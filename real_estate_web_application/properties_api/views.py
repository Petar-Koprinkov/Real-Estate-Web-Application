from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from real_estate_web_application.accounts.models import Profile
from real_estate_web_application.properties_api.serializers import LocationSerializer, ProfileSerializer, \
    ParkingSerializer, PropertySerializer, UserSerializer
from real_estate_web_application.real_estate.models import Location, Properties, Parking

UserModel = get_user_model()


@extend_schema(
    tags=['Users'],
    request=UserSerializer(),
    responses={200: UserSerializer(), 400: UserSerializer()},
)
class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        users = UserModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=['User'],
    request=UserSerializer(),
    responses={200: UserSerializer(), 400: UserSerializer()},
)
class UserListAPIViewSet(APIView):

    @staticmethod
    def get_object(pk: int):
        return get_object_or_404(UserModel, pk=pk)

    @staticmethod
    def get_validation(serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk: int):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk: int):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        return self.get_validation(serializer)

    def patch(self, request, pk: int):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        return self.get_validation(serializer)

    def delete(self, request, pk: int):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
    tags=['Profile'],
    request=ProfileSerializer,
    responses={200: ProfileSerializer, 400: ProfileSerializer},
)
class ProfilesListAPIViewSet(APIView):
    @staticmethod
    def get_profile(pk):
        return get_object_or_404(Profile, pk=pk)

    @staticmethod
    def get_validation(serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        profile = self.get_profile(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk: int):
        profile = self.get_profile(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        return self.get_validation(serializer)

    def patch(self, request, pk: int):
        profile = self.get_profile(pk)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        return self.get_validation(serializer)

    def delete(self, request, pk: int):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
class PropertiesAPIView(APIView):
    def get(self, request, *args, **kwargs):
        properties = Properties.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PropertySerializer(data=request.data)

        if serializer.is_valid():
            my_property = serializer.save(commit=False)
            owner = request.user
            my_property.owner = owner
            my_property.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=['Property'],
    request=PropertySerializer,
    responses={200: PropertySerializer, 400: PropertySerializer},
)
class PropertiesAPIViewSet(APIView):

    @staticmethod
    def get_object(pk):
        return get_object_or_404(Properties, pk=pk)

    def get(self, request, pk: int):
        my_property = self.get_object(pk)
        serializer = PropertySerializer(my_property)
        return Response(serializer.data)
