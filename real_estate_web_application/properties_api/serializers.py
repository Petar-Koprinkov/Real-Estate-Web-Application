from django.contrib.auth import get_user_model
from rest_framework import serializers
from real_estate_web_application.accounts.models import Profile
from real_estate_web_application.real_estate.models import Location, Parking, Properties

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ParkingSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Parking
        fields = '__all__'

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        location = Location.objects.create(**location_data)
        return Parking.objects.create(location=location, **validated_data)


class PropertySerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    parking = ParkingSerializer(read_only=True)

    class Meta:
        model = Properties
        fields = '__all__'
