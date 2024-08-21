from django.db import models

from ledger.models import Account

class City(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField(default = 0.0)
    longitude = models.FloatField(default = 0.0)
    radius = models.FloatField(default = 0.0)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, editable=False)
    
    def save(self, *args, **kwargs):
        a = Account.objects.create()
        self.account = a
        super(City, self).save(*args, **kwargs)

    def __str__(self):
        return self.name  + " with account " + self.account.__str__() + " at lat " + str(self.latitude) + " and long " + str(self.longitude) + " with radius "+ str(self.radius)