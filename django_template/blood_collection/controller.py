from rest_framework.decorators import api_view, permission_classes
from rest_framework.fields import DateField
from rest_framework.views import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ObjectDoesNotExist
from blood_collection.models import BloodCollection
from blood_collection.serializers import BloodCollectionSerializer
from datetime import datetime as dt
import datetime

"""
kontroler za darivanja krvi
"""

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def post_blood_collection(request):
    """
    post ->  dodaje darivanje krvi u sustav
    :param request:
    :return:
    """
    if request.method == "POST":
        serializer = BloodCollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_blood_collection_storage(request, storage=None):
    """
    vraća sve blood collection eventove prema storageu
    :param request:
    :param storage:
    :return:
    """
    if request.method == "GET":
        messages = BloodCollection.objects.all().filter(storage_id = storage )
        serializer = BloodCollectionSerializer(messages, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_valid_blood_collections(request):
    """
    vraća sve blood collection eventove poslije zadanog pocetnog vremena
    :param request:
    :param storage:
    :return:
    """
    if request.method == "GET":
        requested_date = datetime.date.today()
        #requested_date = DateField(year=year, month=month, day=day)
        # https://stackoverflow.com/questions/30366564/daterange-on-a-django-filter
        messages = BloodCollection.objects.all().filter(end_time__gt=requested_date)
        serializer = BloodCollectionSerializer(messages, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)