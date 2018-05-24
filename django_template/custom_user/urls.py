from django.conf.urls import url
from custom_user.views import get_user_details

urlpatterns = [
    url(r'^user_details/', get_user_details)
]