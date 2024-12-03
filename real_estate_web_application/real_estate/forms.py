from django import forms
from real_estate_web_application.real_estate.models import Location, Properties, Parking


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

        error_messages = {
            'city': {
                'required': 'You must enter a city.',
                'max_length': 'Your length have to be maximum 100 characters.',
            },
            'state': {
                'required': 'You must enter a state.',
                'max_length': 'Your length have to be maximum 100 characters.',
            },
            'postcode': {
                'required': 'You must enter a postcode.',
                'max_length': 'Your length have to be maximum 100 characters.',
            }
        }


class ParkingForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = '__all__'


class BasePropertyForm(forms.ModelForm):
    class Meta:
        model = Properties
        exclude = ['owner']


class CreatePropertyForm(BasePropertyForm):
    pass


class EditPropertyForm(BasePropertyForm):
    pass


class SearchPropertyForm(forms.Form):
    property_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Search by Property name...'}),
        label='',
        max_length=100,
        required=False,
    )
