from django.conf.urls import url
from custom_user.views import get_user_details, change_blood_type

urlpatterns = [
    url(r'^user_details/', get_user_details),
    url(r'^change_blood_type/', change_blood_type)
]
