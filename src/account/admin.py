from django.contrib import admin

from .models import ProfileUser


@admin.register(ProfileUser)
class ProfileUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
