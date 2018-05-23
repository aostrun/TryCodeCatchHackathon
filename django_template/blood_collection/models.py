from django.db import models
from blood_storage.models import BloodStorage, BloodStorageItem

# Create your models here.


class BloodCollection(models.Model):
    """
    Blood collection event that collects blood for a certain BloodStorage object
    e.g. Doniranje krvi u Zagrebu u ogranizaciji Crvenog Kriza Zagreb
         storage = Crveni Kriz Zagreb

    """


    name = models.CharField(max_length=50)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    storage = models.ForeignKey(BloodStorage, on_delete=models.DO_NOTHING)

