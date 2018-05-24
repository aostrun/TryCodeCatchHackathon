from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from custom_user.models import User

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_user_id(request):
    """
    vraća sve blood collection eventove prema storageu
    :param request:
    :param storage:
    :return:
    """
    user_id = request.user.id
    return Response(user_id, status=status.HTTP_200_OK)