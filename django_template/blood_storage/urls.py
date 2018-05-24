from django.conf.urls import url
from blood_storage.controller import get_blood_storages, post_blood_storaga

urlpatterns = [
    url(r'^add/$', post_blood_storaga),
    url(r'^get_storages/$', get_blood_storages),
]