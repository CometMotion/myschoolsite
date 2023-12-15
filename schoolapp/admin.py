from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'parent')

admin.site.register(MenuItem, MenuItemAdmin)