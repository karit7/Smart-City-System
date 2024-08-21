from django.db import models
from django.utils import timezone

from .devices import Microphone, Camera, Thermometer, CO2Meter


class Event(models.Model):
    # ABSTRACT CLASS - SHOULDN'T BE INSTANTIATED
    created = models.DateTimeField(auto_now_add=timezone.now())
    
    class Meta:
        ordering = ['created']

    def __str__(self):
        return " event created at " + str(self.created)

class MicrophoneEvent(Event):
    # Django-Audiofield - https://pypi.org/project/django-audiofield/
    # audio = To be implemented
    audioTranscript = models.CharField(max_length= 200)
    microphone = models.ForeignKey(Microphone, on_delete=models.CASCADE)

    def __str__(self):
        return " Microfone audio transcript " + self.audioTranscript + super().__str__()

class CameraEvent(Event):
    # ImageField https://www.geeksforgeeks.org/imagefield-django-models/
    # image = to be implemented
    imageTranscript = models.CharField(max_length= 200)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)

    def __str__(self):
        return " Camera image transcript "+ self.imageTranscript + super().__str__()

class ThermometerEvent(Event):
    temperature = models.FloatField(default=0.0)
    thermometer = models.ForeignKey(Thermometer, on_delete=models.CASCADE)

    def __str__(self):
        return " Temperature " + str(self.temperature) + ' oC.' + super().__str__()

class CO2Event(Event):
    co2Level = models.FloatField(default=0.0)
    co2meter = models.ForeignKey(CO2Meter, on_delete=models.CASCADE)

    def __str__(self):
        return " CO2 level " + str(self.co2Level) + super().__str__()
