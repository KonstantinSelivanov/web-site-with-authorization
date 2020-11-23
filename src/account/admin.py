from django.contrib import admin

from .models import ProfileUser


@admin.register(ProfileUser)
class ProfileUser(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
