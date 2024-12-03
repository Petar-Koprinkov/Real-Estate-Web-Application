from django.test import TestCase

from real_estate_web_application.real_estate.forms import LocationForm


class TestLocationForm(TestCase):
    def setUp(self):
        self.valid_form_data = {
            'city': 'Sofia',
            'state': 'Malinova Dolina',
            'postcode': '1700'
        }

    def test__invalid_required_city_date__returns_error(self):
        self.valid_form_data['city'] = ''
        form = LocationForm(data=self.valid_form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('city', form.errors)

    def test__invalid_max_length_state__returns_error(self):
        self.valid_form_data['city'] = 'a' * 101
        form = LocationForm(data=self.valid_form_data)
        self.assertFalse(form.is_valid())

    def test__valid_required_state__returns_error(self):
        form = LocationForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())
