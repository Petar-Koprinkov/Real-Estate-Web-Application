from django.contrib import admin

from real_estate_web_application.real_estate.models import Properties, Location, Parking


@admin.register(Properties)
class PropertiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'value', 'owner__profile')
    list_filter = ('type', 'value')
    search_fields = ('name',)
    search_help_text = "Search property by name."
    ordering = ('name',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'postcode')
    list_filter = ('city',)
    search_fields = ('city',)
    search_help_text = "Search city by name."
    ordering = ('city', 'state')


@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    list_display = ('parking_name', 'parking_slots', 'location')
    list_filter = ('location',)
    search_fields = ('parking_name',)
    search_help_text = "Search parking by name."
    ordering = ('parking_name', 'parking_slots')
