from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from blood_storage.views import get_storage_sample_size

urlpatterns = [
    url(r'^get_sample_status/$', get_storage_sample_size),
]