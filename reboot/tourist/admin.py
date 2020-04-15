from django.contrib import admin
from .models import Tourist
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Tourist)


