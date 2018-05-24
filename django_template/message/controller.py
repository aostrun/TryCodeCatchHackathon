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

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_user_messages(request, message_to_user=None):
    """
    vraća sve poruke koje su poslane useru
    :param request:
    :return:
    """
    if request.method == "GET":
        messages = Message.objects.all().filter(message_to_user_id = message_to_user )
        serializer = MessageSerializer(messages, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_user_unread_messages(request, message_to_user=None):
    """
    vraća sve nepročitane poruke za usera
    :param request:
    :return:
    """
    if request.method == "GET":
        messages = Message.objects.all().filter(message_to_user_id = message_to_user, is_read=False)
        serializer = MessageSerializer(messages, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def mark_message_as_read(request, message=None):
    """
    poruka.is_read postavlja na true
    :param request:
    :return:
    """
    if request.method == "GET":
        message = Message.objects.get(pk=message)
        message.is_read = True
        message.save()
        return Response(status=status.HTTP_200_OK)