from django.db import models
from custom_user.models import User
from blood_collection.models import BloodCollection


# Create your models here.


class BloodSample(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    volume = models.FloatField(default=1.0)

    event = models.ForeignKey(BloodCollection, on_delete=models.DO_NOTHING)

    date_collected = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.username + ": " + self.event.name + ": " + str(self.volume)