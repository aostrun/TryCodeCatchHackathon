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
@permission_classes((AllowAny, ))
def get_blood_samples(request, event_id=None):

    if event_id == None:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    print(BloodCollection.objects.get(id=1).name)

    samples = BloodSample.objects.all().filter(event_id=event_id)
    serializer = BloodSampleSerializer(samples, many=True, context={'request':request})

    return Response(data=serializer.data, status=status.HTTP_200_OK)

    #return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((AllowAny, ))
def add_blood_sample(request):


    sample = BloodSample.objects.create(
                            user_id=int(request.POST.get('user_id')),
                            event_id=int(request.POST.get('event_id')),
                            volume=float(request.POST.get('volume'))
                                        )

    sample.save()
    serializer = BloodSampleSerializer(data=sample)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)