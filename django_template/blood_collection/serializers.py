from rest_framework import serializers
from blood_collection.models import BloodCollection


class BloodCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodCollection
        fields = ("name", "start_time", "end_time", "location_lat", "location_lon", "storage")
