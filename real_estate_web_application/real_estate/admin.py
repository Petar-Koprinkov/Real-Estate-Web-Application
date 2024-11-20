from django.contrib import admin

from real_estate_web_application.real_estate.models import Properties


@admin.register(Properties)
class PropertiesAdmin(admin.ModelAdmin):
    pass
