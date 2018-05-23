from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class User(AbstractUser):

    #blood type choices
    BLOOD_TYPE_CHOICES = (
        ("0-", "0-"),
        ("0+", "0+"),
        ("A-", "A-"),
        ("A+", "A+"),
        ("B-", "B-"),
        ("B+", "B+"),
        ("AB-", "AB-"),
        ("AB+", "AB+")
        #---
    )
    blood_type = models.CharField( choices=BLOOD_TYPE_CHOICES)

    phone_number = models.CharField(max_length=14)

    #sex choices
    SEX_CHOICES = (
        ("M", "Male"),
        ("F", "Female")
        #---
    )
    sex = models.CharField(choices=SEX_CHOICES)

    date_of_birth = models.DateField()

    location_lat = models.FloatField()
    location_lon = models.FloatField()

    last_donation = models.DateTimeField()
    
    distance = models.FloatField()
