from rest_framework import serializers
from message.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("message_body", "message_from_user", "message_to_user", "is_read")