from django.contrib.auth.models import Group
from django.test import TestCase
from real_estate_web_application.real_estate.models import Location, Parking, Properties


class TestLocationModel(TestCase):

    def setUp(self):
        self.credential_location = {
            'city': 'Nova Zagora',
            'state': 'Centur',
            'postcode': 1700
        }

    def test__valid_str_method(self):
        location = Location(**self.credential_location)
        self.assertEqual(str(location), f'{location.city}, {location.state}')
