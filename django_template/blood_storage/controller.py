from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from blood_storage.models import BloodStorage
from blood_storage.serializers import BloodStorageSerializer


"""
kontroler za blood storage
"""


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def post_blood_storaga(request):
    """
    post ->  dodaje blood storage u sustav
    :param request:
    :return:
    """
    if request.method == "POST":
        serializer = BloodStorageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_blood_storages(request):
    """
    vraća sve blood collection eventove prema storageu
    :param request:
    :param storage:
    :return:
    """
    if request.method == "GET":
        storages = BloodStorage.objects.all()
        serializer = BloodStorageSerializer(storages, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
