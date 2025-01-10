from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from real_estate_web_application.accounts.models import Profile
from real_estate_web_application.properties_api.serializers import LocationSerializer, ProfileSerializer, \
    ParkingSerializer, PropertySerializer
from real_estate_web_application.real_estate.models import Location, Properties, Parking


@extend_schema(
    tags=['Profiles'],
    request=ProfileSerializer,
    responses={200: ProfileSerializer, 400: ProfileSerializer},
)
class ProfileAPIView(APIView):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)


@extend_schema(
    tags=['Locations'],
    request=LocationSerializer,
    responses={200: LocationSerializer, 400: LocationSerializer},
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
    tags=['Location'],
    request=LocationSerializer,
    responses={200: LocationSerializer, 404: LocationSerializer},
)
class LocationListAPIViewSet(APIView):
    @staticmethod
    def get_object(pk):
        return get_object_or_404(Location, pk=pk)

    @staticmethod
    def valid_serializer(serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk: int):
        location = self.get_object(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def put(self, request, pk: int):
        location = self.get_object(pk)
        serializer = LocationSerializer(location, data=request.data)

        return self.valid_serializer(serializer)

    def patch(self, request, pk: int):
        location = self.get_object(pk)
        serializer = LocationSerializer(location, request.data, partial=True)

        return self.valid_serializer(serializer)

    def delete(self, request, pk: int):
        location = self.get_object(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(
    tags=['Parking Lots'],
    request=ParkingSerializer,
    responses={200: ParkingSerializer, 400: ParkingSerializer},
)
class ParkingAPIView(APIView):
    def get(self, request, *args, **kwargs):
        parkings = Parking.objects.all()
        serializer = ParkingSerializer(parkings, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ParkingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=['Parking Lot'],
    request=ParkingSerializer,
    responses={200: ParkingSerializer, 400: ParkingSerializer},
)
class ParkingAPIViewSet(APIView):

    @staticmethod
    def get_object(pk):
        return get_object_or_404(Parking, pk=pk)

    @staticmethod
    def valid_serializer(serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk: int):
        parking = self.get_object(pk)
        serializer = ParkingSerializer(parking)
        return Response(serializer.data)

    def put(self, request, pk: int):
        parking = self.get_object(pk)
        serializer = ParkingSerializer(parking, data=request.data)

        return self.valid_serializer(serializer)

    def patch(self, request, pk: int):
        parking = self.get_object(pk)
        serializer = ParkingSerializer(parking, request.data, partial=True)

        return self.valid_serializer(serializer)

    def delete(self, request, pk: int):
        parking = self.get_object(pk)
        parking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@extend_schema(
    tags=['Properties'],
    request=PropertySerializer,
    responses={200: PropertySerializer},
)
class PropertiesAPIView(ListAPIView):
    queryset = Properties.objects.all()
    serializer_class = PropertySerializer
