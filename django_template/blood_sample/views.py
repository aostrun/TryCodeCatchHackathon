from django.shortcuts import render
from blood_sample.models import BloodSample
from blood_collection.models import BloodCollection
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from blood_sample.serializers import BloodSampleSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET'])
@permission_classes((AllowAny))
def get_blood_samples(request, event_id=None):

    if event_id == None:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    samples = BloodSample.objects.all().filter(event_id=event_id)
    serializer = BloodSampleSerializer(data=samples, many=True, context={'request':request})

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((AllowAny))
def add_blood_sample(request, user_id=None, event_id=None):

    if event_id == None or user_id == None:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = BloodSampleSerializer.create(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)