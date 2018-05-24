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
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES, null=True)

    phone_number = models.CharField(max_length=14, null=True)

    #sex choices
    SEX_CHOICES = (
        ("M", "Male"),
        ("F", "Female")
        #---
    )
    sex = models.CharField(max_length=30, choices=SEX_CHOICES, null=True)

    date_of_birth = models.DateField(null=True)

    location_lat = models.FloatField(null=True)
    location_lon = models.FloatField(null=True)

    last_donation = models.DateTimeField(null=True)

    #days_past = models.IntegerField(null=True)

    distance = models.FloatField(null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name