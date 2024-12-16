from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from real_estate_web_application.accounts.models import Profile
from real_estate_web_application.properties_api.serializers import LocationSerializer, ProfileSerializer, \
    ParkingSerializer, PropertySerializer
from real_estate_web_application.real_estate.models import Location, Properties, Parking


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
class LocationAPIView(APIView):
    def get(self, request, *args, **kwargs):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = LocationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=['Parking Lots'],
    request=ParkingSerializer,
    responses={200: ParkingSerializer},
)
class ParkingAPIView(ListAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer


@extend_schema(
    tags=['Properties'],
    request=PropertySerializer,
    responses={200: PropertySerializer},
)
class PropertiesAPIView(ListAPIView):
    queryset = Properties.objects.all()
    serializer_class = PropertySerializer
