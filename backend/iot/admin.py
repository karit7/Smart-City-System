from django.contrib import admin

from .models import City
from .models import Role, Resident, Visitor
from .models import StreetSign, InformationKiosk
from .models import Camera, CameraEvent, Microphone, MicrophoneEvent, Thermometer, ThermometerEvent, CO2Meter, CO2Event, InputSensor

# Register your models here.
admin.site.register(City)
admin.site.register(Role)
admin.site.register(Resident)
admin.site.register(Visitor)
admin.site.register(StreetSign)
admin.site.register(InformationKiosk)
admin.site.register(Camera)
admin.site.register(CameraEvent)
admin.site.register(Microphone)
admin.site.register(MicrophoneEvent)
admin.site.register(Thermometer)
admin.site.register(ThermometerEvent)
admin.site.register(CO2Meter)
admin.site.register(CO2Event)