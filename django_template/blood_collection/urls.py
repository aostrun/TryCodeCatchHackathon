from django.conf.urls import url
from blood_collection.controller import post_blood_collection, get_blood_collection_storage,get_valid_blood_collections

urlpatterns = [
    url(r'^add/$', post_blood_collection),
    url(r'^get_storage/(?P<storage>\w+)$', get_blood_collection_storage),
    url(r'^get_valid/$', get_valid_blood_collections)
]