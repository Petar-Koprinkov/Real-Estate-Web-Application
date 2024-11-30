from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from real_estate_web_application.real_estate.forms import CreatePropertyForm
from real_estate_web_application.real_estate.models import Location, Parking

UserModel = get_user_model()


class TestAddPropertyView(TestCase):
    def setUp(self):

        self.credential_owner = {
            'username': 'pkoprinkov11',
            'password': '56932957eH10'
        }

        self.credential_location = {
            'city': 'Nova Zagora',
            'state': 'Centur',
            'postcode': 1700
        }

        location = Location.objects.create(**self.credential_location)

        self.credential_parking = {
            'parking_name': 'Centur Parking',
            'parking_slots': 10,
            'location': location
        }

        parking = Parking.objects.create(**self.credential_parking)

        self.credential_property = {
            'name': 'Maria Rose',
            'type': 'Two-Bedroom Apartment',
            'property_image': 'https://media.geeksforgeeks.org/wp-content/uploads/20240611173741/Integration-Testing.webp',
            'floors': 4,
            'exposure': 'North',
            'value': 400_000,
            'location': location,
            'parking': parking,
            'content': 'Very nice!'
        }

    def test__form_create_property__returns_valid_form(self):
        user = UserModel.objects.create_user(**self.credential_owner)
        self.client.login(**self.credential_owner)
        form = CreatePropertyForm(data=self.credential_property)

        form.save(commit=False)
        form.instance.owner = user

        response = self.client.post(reverse('add-property'))

        self.assertEqual(form.instance.owner, user)








