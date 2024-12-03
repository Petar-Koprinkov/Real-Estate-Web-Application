from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase

from real_estate_web_application.common.models import CommentModel
from real_estate_web_application.real_estate.models import Location, Parking, Properties

ModelUser = get_user_model()


class TestCommentModel(TestCase):
    def setUp(self):
        self.seller_group = Group.objects.create(name='Seller')
        self.buyer_group = Group.objects.create(name='Buyer')
        self.buyer_group = Group.objects.create(name='Broker')
        self.buyer_group = Group.objects.create(name='Investor')

        self.credential_owner = {
            'username': 'pkoprinkov11',
            'password': '569hfjkjhg3295hfkjhjkg7eH10',
            'user_type': 'Investor'
        }

        user = ModelUser(**self.credential_owner)

        self.credential_location = {
            'city': 'Nova Zagora',
            'state': 'Centur',
            'postcode': 1700
        }

        location = Location(**self.credential_location)

        self.credential_parking = {
            'parking_name': 'Centur Parking',
            'parking_slots': 10,
            'location': location
        }

        parking = Parking(**self.credential_parking)

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

        my_property = Properties(**self.credential_property)

        self.credential_comment = {
            'comment': 'Very nice!',
            'property': my_property,
            'user': user,
        }

    def test__valid_str_method(self):
        comment = CommentModel(**self.credential_comment)
        self.assertEqual(str(comment), comment.comment)



