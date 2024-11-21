from django import forms
from real_estate_web_application.real_estate.models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
