from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.
class CustomAdmin(UserAdmin):
    model=CustomUser

admin.site.register(CustomUser,CustomAdmin)