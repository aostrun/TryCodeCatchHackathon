from django.contrib.auth import get_user_model
from rest_framework import serializers, models
# from views import
UserModel = get_user_model()
from allauth.account.utils import setup_user_email
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import PasswordResetSerializer


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    location_lat = serializers.FloatField()
    location_lon = serializers.FloatField()

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        }

    def custom_signup(self, request, user):
        print(request.POST.get('location_lat'))
        user.location_lat = float(request.POST.get('location_lat'))
        user.location_lon = float(request.POST.get('location_lon'))
        user.blood_type = request.POST.get('blood_type')
        user.sex = request.POST.get('sex')
        user.save()