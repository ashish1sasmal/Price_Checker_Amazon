from django.contrib import admin

from .models import Profile,Products,ControlRoom
# Register your models here.

admin.site.register(Profile)
admin.site.register(Products)
admin.site.register(ControlRoom)
