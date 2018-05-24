import geopy.distance
from blood_storage.models import BloodStorage

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


def get_closest_blood_storage(request, current_storage_id=None, blood_type=None):

    if current_storage_id == None or blood_type == None:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    current_storage = BloodStorage.objects.get()
    storages = BloodStorage.objects.all()
    min_distance = geopy.distance.vincenty( () , ).km
    for storage in storages:
        if storage.id != current_storage.id:




