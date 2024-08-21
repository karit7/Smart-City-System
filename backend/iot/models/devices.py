from django.db import models
from django.contrib.auth import get_user_model

from .city import  City

from ledger.models import Transaction

# ------ Input sensors --------

class InputSensor(models.Model):
    # ABSTRACT CLASS - SHOULDN'T BE INSTANTIATED
    device = models.ForeignKey('Device', on_delete=models.CASCADE)

    def __str__(self):
        return " sensor with id " + str(self.id) + " at device " + str(self.device.__str__())

class Microphone(InputSensor):
    def __str__(self):
        return " Microphone "  + super().__str__()

class Thermometer(InputSensor):
    def __str__(self):
        return " Thermometer " + super().__str__()

class CO2Meter(InputSensor):
    def __str__(self):
        return " Co2 Meter " + super().__str__()

class Camera(InputSensor):
    def __str__(self):
        return " Camera " + super().__str__()

# ------ Output sensors --------
class OutputSensor(models.Model):
    # ABSTRACT CLASS - SHOULDN'T BE INSTANTIATED
    device = models.ForeignKey('Device', on_delete=models.CASCADE)

    def __str__(self):
        return " output sensor with id " + str(self.id) + " at device " + str(self.device.__str__())

class Speaker(OutputSensor):
    audioTranscript = models.CharField(max_length= 200)
    
    def __str__(self):
        return " Speaker audio transcript " + self.audioTranscript + super().__str__()

# ------ Devices --------

class DeviceStatus(models.TextChoices):
    WORKING = 'W', 'Working'
    NOT_WORKING = 'NW', 'Not Working'
    UNDER_MAINTENANCE = 'UM', 'Under Maintenance'

class Device(models.Model):
    # ABSTRACT CLASS - SHOULDN'T BE INSTANTIATED
    latitude = models.FloatField(default = 0.0)
    longitude = models.FloatField(default = 0.0)
    status = models.CharField(max_length=2, choices=DeviceStatus.choices, default=DeviceStatus.WORKING)
    enabled = models.BooleanField(default=True)
    
    @property
    def city(self):
        cities = City.objects.all()
        city = 0
        smallest_distance = 1e15
        for city in cities:
            distance = ((city.latitude - self.latitude)**2 + (city.longitude - self.longitude)**2)**0.5
            if distance < city.radius:
                return city
        
        # if the device is not in the radius of any city, return the first city in the db
        # CORRECT THIS!
        return cities[0]

    @property
    def account(self):
        return self.city.account

    def get_name(self):
        return 'Device'

    def __str__(self):
        return self.get_name() + " at lat " + str(self.latitude) + " and long " + str(self.longitude) + " with status "+ DeviceStatus(self.status).label + " enabled " + str(self.enabled)

class StreetSign(Device):
    text = models.CharField(max_length= 200)

    def get_name(self):
        return 'Street Sign'

    def __str__(self):
        return super().__str__() + " with text " + self.text

class InformationKiosk(Device):
    
    def purchase_ticket(self, person, event):
        # The Kiosk can also support purchasing tickets for concerts and other events.
        
        # create a transaction - payer is person and receiver is city
        amount = event.price
        payer = person.account
        receiver = self.city.account
        note = " Ticket to event " + event.__str__()
        ticket_transaction = Transaction.objects.create(amount=amount, payer=payer, receiver=receiver, note=note)
        
        # try to process the transaction and return (True if was processed or False if created but still in draft mode)
        return ticket_transaction.process()
    
    def get_name(self):
        return 'Information Kiosk'

    def __str__(self):
        return "Information Kiosk " + super().__str__()

class StreetLight(Device):
    brightness = models.FloatField(default=1.0)

    def get_name(self):
        return 'Street Light'

    def __str__(self):
        return "Street Light " + super().__str__()

class Robot(Device):

    def get_name(self):
        return 'Robot'

    def __str__(self):
        return "Robot " + super().__str__()

class ParkingSpace(Device):

    fee = models.FloatField(default=0.0)
    
    def get_name(self):
        return 'Parking Space'

    def charge(self, vehicle, hours):
        # A parking space has an hourly rate which is charged
        # to the account associated with the vehicle.
        
        # create a transaction - payer is person and receiver is city
        amount = hours * self.price
        payer = vehicle.owner.account
        receiver = self.city.account
        note = " Parking fee relative to " + hours + " hours."
        parking_transaction = Transaction.objects.create(amount=amount, payer=payer, receiver=receiver, note=note)
        
        # try to process the transaction and return (True if was processed or False if created but still in draft mode)
        return parking_transaction.process()

    def __str__(self):
        return "Parking Space " + super().__str__()

class VehicleType(models.TextChoices):
    BUS = 'B', 'Bus'
    CAR = 'C', 'Car'

class Vehicle(Device):

    vehicleType = models.CharField(max_length=1, choices=VehicleType.choices, default=VehicleType.CAR)
    maximumCapacity = models.IntegerField(default=1)
    fee = models.FloatField(default=0.0)
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def get_name(self):
        return 'Vehicle'

    def charge(self, person):
        # Riding in a Bus or Car is free for Visitors, 
        # but requires a fee for Residents.
        # create a transaction - payer is person and receiver is city
        amount = self.fee
        payer = person.account
        receiver = self.city.account
        note = " Transport fee"
        boarding_transaction = Transaction.objects.create(amount=amount, payer=payer, receiver=receiver, note=note)
        
        # try to process the transaction and return (True if was processed or False if created but still in draft mode)
        return boarding_transaction.process()

    def __str__(self):
        return "Parking Space " + super().__str__()