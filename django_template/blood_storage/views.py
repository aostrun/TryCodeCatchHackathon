from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from blood_storage.models import BloodStorage
from blood_sample.models import BloodSample

# Create your views here.


@api_view(['GET',])
def get_storage_sample_size(request, storage_id):
    storage_samples = BloodSample.objects.all().filter(event__storage_id=storage_id)
    #storage_samples.filter(co)


