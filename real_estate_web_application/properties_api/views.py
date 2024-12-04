from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from real_estate_web_application.accounts.models import Profile
from real_estate_web_application.properties_api.serializers import LocationSerializer, ProfileSerializer, \
    ParkingSerializer, PropertySerializer
from real_estate_web_application.real_estate.models import Location, Properties


@extend_schema(
    tags=['Profiles'],
    request=ProfileSerializer,
    responses={200: ProfileSerializer},
)
class ProfileAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


@extend_schema(
    tags=['Locations'],
    request=LocationSerializer,
    responses={200: LocationSerializer},
)
class LocationAPIView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


@extend_schema(
    tags=['Parkings'],
    request=ParkingSerializer,
    responses={200: ParkingSerializer},
)
class ParkingAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ParkingSerializer


@extend_schema(
    tags=['Properties'],
    request=PropertySerializer,
    responses={200: PropertySerializer},
)
class PropertiesAPIView(ListAPIView):
    queryset = Properties.objects.all()
    serializer_class = PropertySerializer