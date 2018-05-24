from django.conf.urls import url
from custom_user.views import get_user_id

urlpatterns = [
    url(r'^user_id/', get_user_id)
]