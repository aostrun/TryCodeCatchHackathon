import time
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ObjectDoesNotExist
from message.models import Message
from message.serializers import MessageSerializer

"""
kontroler za poruke
"""

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def post_user_message(request):
    """
    post ->  dodaje poruku za odredenog usera od usera
    :param request:
    :return:
    """
    if request.method == "POST":
        # print(User.objects.get(username="admin").id)
        # comment = Comment.objects.create(user_id_id= request.POST.get('user_id'),
        #  comment_body=request.POST.get('comment_body'))
        # comment.save()
        # return Response(comment, status=status.HTTP_201_CREATED)
        #
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
