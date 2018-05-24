from django.conf.urls import url
from message.controller import post_user_message, get_user_messages, get_user_unread_messages, mark_message_as_read


urlpatterns = [
    url(r'^add/$', post_user_message),
    url(r'^mark_as_read/(?P<message>\w+)$', mark_message_as_read),
    url(r'^get/(?P<message_to_user>\w+)$', get_user_messages),
    url(r'^get_unread/(?P<message_to_user>\w+)$', get_user_unread_messages),
]