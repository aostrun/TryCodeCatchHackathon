import geopy.distance
from blood_storage.models import BloodStorage
from blood_storage.serializers import BloodStorageSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


def get_closest_blood_storage(request, current_storage_id=None, blood_type=None):

    if current_storage_id == None or blood_type == None:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    current_storage = BloodStorage.objects.get(pk=current_storage_id)
    storages = BloodStorage.objects.all()
    min_idx = 0
    if(storages[0].id != current_storage_id):
        min_distance = geopy.distance.vincenty( (current_storage.location_lon, current_storage.location_lat) , (storages[0].location_lon, storages[0].location_lat)).km
    else:
        min_distance = geopy.distance.vincenty( (current_storage.location_lon, current_storage.location_lat) , (storages[1].location_lon, storages[1].location_lat)).km
        min_idx = 1
    for i in range(1, len(storages)):
        if storages[i] != current_storage.id and storages[i].get_blood_volume(blood_type):
            distance = geopy.distance.vincenty( (current_storage.location_lon, current_storage.location_lat) , (storages[i].location_lon, storages[i].location_lat)).km
            if(distance < min_distance):
                min_distance = distance


    serializer = BloodStorageSerializer(data=storages[min_idx])

    return Response(data=serializer.data, status=status.HTTP_200_OK)


