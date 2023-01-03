from django.contrib import admin
from .models import MenuGroup, MenuItem, Logo


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    pass


@admin.register(MenuGroup)
class MenuGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    pass
