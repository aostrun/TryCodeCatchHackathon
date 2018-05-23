from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from blood_sample.views import get_blood_samples, add_blood_sample


urlpatterns = [
    url(r'^get/(?P<event_id>\w+)/$', get_blood_samples),
    url(r'^add/', add_blood_sample)
]