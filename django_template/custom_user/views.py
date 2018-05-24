from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from custom_user.models import User

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_user_details(request):
    """
    vraća detalje usera
    :param request:
    :param storage:
    :return:
    """
    user_details = {}

    user_id = request.user.id
    user_details["user_id"] = user_id
    user = User.objects.get(pk = user_id)
    user_details["first_name"] = user.first_name
    user_details["last_name"] = user.last_name
    user_details["blood_type"] = user.blood_type
    user_details["sex"] = user.sex
    return Response(user_details, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def change_blood_type(request):
    """
    mijenjanje krvne grupe za usera
    :param request:
    :return:
    """

    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        blood_type = request.POST.get("blood_type")
        user.blood_type = blood_type
        user.save()
        return Response(status=status.HTTP_200_OK)


