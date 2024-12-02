from django.contrib.auth import get_user_model
from django.test import TestCase
from django.contrib.auth.models import Group

from real_estate_web_application.accounts.models import Profile

ModelUser = get_user_model()


class TestProfileModel(TestCase):
    def setUp(self):
        self.seller_group = Group.objects.create(name='Seller')
        self.buyer_group = Group.objects.create(name='Buyer')
        self.broker_group = Group.objects.create(name='Broker')
        self.investor_group = Group.objects.create(name='Investor')

        self.credential_user = {
            'username': 'pkoprinkov11',
            'password': '56932957eH10',
            'user_type': 'Investor'
        }

    def test__valid_str_method(self):
        user = ModelUser.objects.create_user(**self.credential_user)

        profile, created = Profile.objects.get_or_create(
            user=user,
            defaults={
                'first_name': 'Petar',
                'last_name': 'Koprinkov',
                'email': 'petur_koprinkov@abv.bg',
                'profile_picture': None,
            }
        )

        self.assertEqual(str(profile), f"{profile.first_name} {profile.last_name}")
