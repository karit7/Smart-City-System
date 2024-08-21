# python manage.py shell < generate_data.py

# ledger app
from ledger.models import Account, Transaction, TransactionStatus

# Create 2 accounts
payer = Account.objects.create(balance = 1000.0)
receiver = Account.objects.create(balance = 0.0)

# Create 2 transaction
t1 = Transaction.objects.create(amount = 100,
                            payer = payer,
                            receiver = receiver,
                            note = "A test transaction")
t2 = Transaction.objects.create(amount = 300,
                            payer = payer,
                            receiver = receiver,
                            note = "A second test transaction")

# Process the first transaction
t1.process()

from iot.models import City
from iot.models import DeviceStatus, StreetSign

City.objects.create(name= 'Rio de Janeiro', account = payer, latitude = -22.9035, longitude=-43.2096, radius=1)
City.objects.create(name= 'New York', account = receiver, latitude = 40.7128, longitude=74.0060, radius=1)

# device located in Rio (dynamically found through the location)
streetSign = StreetSign.objects.create(latitude = -22.9035, longitude = -43.2096, status = DeviceStatus.WORKING, enabled = True)

from iot.models import Microphone, Thermometer, CO2Meter, Camera
from iot.models import Speaker

Microphone.objects.create(device = streetSign)
Thermometer.objects.create(device = streetSign)
CO2Meter.objects.create(device = streetSign)
Camera.objects.create(device = streetSign)
Speaker.objects.create(device = streetSign)

# device located in New York (dynamically found through the location)
s2 = StreetSign.objects.create(latitude = 40.7128, longitude=75.0000, status = DeviceStatus.WORKING, enabled = True)
print(s2.city)


'''
from iot.models import Role, Resident, Visitor
from iot.models import StreetSign, Status, InformationKiosk, StreetLight
from iot.models import Camera, CameraEvent, Microphone, MicrophoneEvent, Thermometer, ThermometerEvent, CO2Meter, CO2Event, InputSensor


adult_role = Role.objects.create(name = "adult_role")
Resident.objects.create(name = "John" ,phone = "21-3333-4444", role=adult_role)
Resident.objects.create(name = "Mary" ,phone = "21-3332-4242", role=adult_role)
Visitor.objects.create()

city_dubai = City.objects.create(name="Dubai")

device_streetSign = StreetSign(status=Status.WORKING, 
enabled = True, city_holder=city_dubai, text = "Speed limit 80 km/h")
device_streetSign.save()

device_infoKiosk = InformationKiosk(status=Status.WORKING, 
enabled = True, city_holder=city_dubai)
device_infoKiosk.save()

device_streetLight = StreetLight(status=Status.WORKING, 
enabled = True, city_holder=city_dubai, brightness = 1.0)
device_streetLight.save()

Camera.objects.create(device = device_infoKiosk)
Microphone.objects.create(device = device_infoKiosk)
Thermometer.objects.create(device = device_infoKiosk)
CO2Meter.objects.create(device = device_infoKiosk)
'''