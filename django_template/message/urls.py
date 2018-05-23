from django.conf.urls import url
from message.controller import post_user_message


urlpatterns = [
    url(r'^add/$', post_user_message),
    # url(r'^comment/get/$', get_user_comment),

]