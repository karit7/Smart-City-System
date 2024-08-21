from ledger.serializers import AccountSerializer
from rest_framework import serializers
from .models import City
from .models import InformationKiosk, ParkingSpace, StreetSign, StreetLight, Robot, Vehicle

from .models import Camera, Microphone, CO2Meter, Thermometer
from .models import Speaker

class CitySerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    class Meta:
        model = City
        fields = '__all__'

# ------- DEVICES ----------------------------------------
class InformationKioskSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    class Meta:
        model = InformationKiosk
        fields = '__all__'
        
class ParkingSpaceSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    class Meta:
        model = ParkingSpace
        fields = '__all__'

class StreetSignSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    class Meta:
        model = StreetSign
        fields = '__all__'
        read_only_fields = ['camera_set', 'microphone_set', 'thermometer_set', 'co2meter_set', 'speaker_set']

class StreetLightSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    class Meta:
        model = StreetLight
        fields = '__all__'

class RobotSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    class Meta:
        model = Robot
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    class Meta:
        model = Vehicle
        fields = '__all__'