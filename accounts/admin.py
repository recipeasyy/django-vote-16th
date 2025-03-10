from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'part', 'team']
    list_display_links = ['name', 'part', 'team']
