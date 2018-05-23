from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class CustomUserInline(admin.StackedInline):
    model = User


class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + ( ('Location', {'fields': ('location_lat', 'location_lon', 'distance', )}),
                                        ('Gender', {'fields': ('sex',)}),
                                        ('Blood', {'fields': ('blood_type', 'last_donation')}),

                                        )

admin.site.register(User, CustomUserAdmin)