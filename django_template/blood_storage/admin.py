from django.contrib import admin
from blood_storage.models import BloodStorage, BloodStorageItem, BloodTypeRange
# Register your models here.

admin.site.register(BloodStorage)
admin.site.register(BloodStorageItem)
admin.site.register(BloodTypeRange)