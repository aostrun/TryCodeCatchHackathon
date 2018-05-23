from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models



# Create your models here.

class User(AbstractUser):

    BLOOD_TYPE_CHOICES = (
        ("0-", "0-"),
        #---
    )
    blood_type = models.CharField(max=3, choices=BLOOD_TYPE_CHOICES)

    score = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=14)

    SEX_CHOICES = (
        ("M", "M")
        #---
    )
    sex = models.CharField(choices=SEX_CHOICES)

    date_of_birth = models.DateField()

    location = models.PointField()

    last_donation = models.DateTimeField()
    
    distance = models.FloatField()
