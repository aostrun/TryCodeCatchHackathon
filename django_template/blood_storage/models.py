from django.db import models

# Create your models here.




class BloodStorage(models.Model):

    name = models.CharField(max_length=50)

    location_lon = models.FloatField(null=True)
    location_lat = models.FloatField(null=True)

    def __str__(self):
        return self.name




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

