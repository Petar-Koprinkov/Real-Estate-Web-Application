from django.test import TestCase

from real_estate_web_application.real_estate.models import Location, Parking


class TestParkingModel(TestCase):

    def setUp(self):

        self.credential_location = {
            'city': 'Nova Zagora',
            'state': 'Centur',
            'postcode': 1700
        }

        location = Location(**self.credential_location)

        self.credential_parking = {
            'parking_name': 'Centur Parking',
            'parking_slots': 10,
            'location': location,
        }

    def test__valid_str_method(self):
        parking = Parking(**self.credential_parking)
        self.assertEqual(str(parking), parking.parking_name)
