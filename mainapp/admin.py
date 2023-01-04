from django.contrib import admin
from .models import MenuGroup


@admin.register(MenuGroup)
class MenuGroupAdmin(admin.ModelAdmin):
    pass
