from django.db import models
#from blood_sample.models import BloodSample
import datetime

# Create your models here.



class BloodStorage(models.Model):

    name = models.CharField(max_length=50)

    location_lon = models.FloatField(null=True)
    location_lat = models.FloatField(null=True)

    def __str__(self):
        return self.name


    def get_blood_volume(self, blood_type):
        storage_collections = self.bloodcollection_set

        for collection in storage_collections:
            storage_samples = collection.bloodsample_set
            # current_datetime = datetime.datetime.today()
            current_datetime = datetime.datetime.today() - datetime.timedelta(days=30)

            volume_by_type = {

                "0-": 0,
                "0+": 0,
                "A-": 0,
                "A+": 0,
                "B-": 0,
                "B+": 0,
                "AB-": 0,
                "AB+": 0

            }

            storage_samples.filter(date_collected__gte=current_datetime)
            for sample in storage_samples:
                volume_by_type[sample.user.blood_type] += sample.volume

            return volume_by_type[blood_type]

class BloodTypeRange(models.Model):

    BLOOD_TYPE_CHOICES = (
        ("0-", "0-"),
        ("0+", "0+"),
        ("A-", "A-"),
        ("A+", "A+"),
        ("B-", "B-"),
        ("B+", "B+"),
        ("AB-", "AB-"),
        ("AB+", "AB+")
        # ---
    )
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES, null=True)

    storage_id = models.ForeignKey(BloodStorage, on_delete=models.CASCADE)

    min_value = models.FloatField(null=True)
    max_value = models.FloatField(null=True)






class BloodStorageItem(models.Model):
    """
    Item that is stored at the BloodStorage object
    e.g. A+ blood type, 5L volume at storage
    """

    # blood type choices
    BLOOD_TYPE_CHOICES = (
        ("0-", "0-"),
        ("0+", "0+"),
        ("A-", "A-"),
        ("A+", "A+"),
        ("B-", "B-"),
        ("B+", "B+"),
        ("AB-", "AB-"),
        ("AB+", "AB+")
        # ---
    )
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES, null=True)

    volume = models.FloatField(default=0.0)

    storage = models.ForeignKey(BloodStorage, on_delete=models.CASCADE)


    def __str__(self):
        return self.storage.name + ": " + self.blood_type + " - " + str(self.volume)

