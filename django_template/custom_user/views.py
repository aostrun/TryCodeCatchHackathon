from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from custom_user.models import User

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_user_details(request):
    """
    vraća sve blood collection eventove prema storageu
    :param request:
    :param storage:
    :return:
    """
    user_details = {}

    user_id = request.user.id
    user_details["user_id"] = user_id
    user = User.objects.get(pk = user_id)
    print(user)
    user_details["first_name"] = user.first_name
    user_details["last_name"] = user.last_name
    user_details["blood_type"] = user.blood_type
    user_details["sex"] = user.sex

    return Response(user_details, status=status.HTTP_200_OK)

