from django import forms
from real_estate_web_application.real_estate.models import Location, Properties


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class BasePropertyForm(forms.ModelForm):
    class Meta:
        model = Properties
        exclude = ['owner']


class CreatePropertyForm(BasePropertyForm):
    pass