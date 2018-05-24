from rest_framework import serializers
from message.models import Message
from custom_user.serializers import CustomRegisterSerializer



class MessageSerializer(serializers.ModelSerializer):

    message_from = CustomRegisterSerializer(source="message_from_user")
    message_to = CustomRegisterSerializer(source="message_to_user")

    class Meta:
        model = Message
        fields = ("id", "message_body", "message_from", "message_to", "is_read")


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Message.objects.create(**validated_data)