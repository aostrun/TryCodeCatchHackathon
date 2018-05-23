from rest_framework import serializers
from blood_sample.models import BloodSample


class BloodSampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = BloodSample
        fields = '__all__'