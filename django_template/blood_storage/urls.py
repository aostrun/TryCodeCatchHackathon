from django.conf.urls import url
from blood_storage.controller import get_blood_storages, post_blood_storaga
from blood_storage.views import get_storage_sample_size

urlpatterns = [
    url(r'^get_sample_status/(?P<storage_id>\w+)/$', get_storage_sample_size),
    url(r'^add/$', post_blood_storaga),
    url(r'^get_storages/$', get_blood_storages),
]