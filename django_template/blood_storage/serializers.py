from rest_framework import serializers
from blood_storage.models import BloodStorage

class BloodStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodStorage
        fields = ("id", "name", "location_lon", "location_lat")
