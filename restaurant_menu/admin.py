from django.contrib import admin
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    # these are in models.py
    list_display = ("meal", "status")
    list_filter = ("status",)
    search_fields = ("meal", "description")


# register the class
admin.site.register(MenuItem, MenuItemAdmin)
