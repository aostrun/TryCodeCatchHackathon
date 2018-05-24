import datetime

from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from blood_storage.models import BloodStorage
from blood_sample.models import BloodSample
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET',])
def get_storage_sample_size(request, storage_id):
    storage_samples = BloodSample.objects.all().filter(event__storage_id=storage_id)
    current_datetime = datetime.datetime.today()
    current_datetime.month -= 1

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


    return Response(volume_by_type, status=status.HTTP_200_OK)



