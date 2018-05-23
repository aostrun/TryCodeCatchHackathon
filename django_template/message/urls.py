from django.conf.urls import url
from message.controller import post_user_message, get_user_messages, get_user_unread_messages


urlpatterns = [
    url(r'^add/$', post_user_message),
    url(r'^get/(?P<message_to_user>\w+)$', get_user_messages),
    url(r'^get_unread/(?P<message_to_user>\w+)$', get_user_unread_messages),
]