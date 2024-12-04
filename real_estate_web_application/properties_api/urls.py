from django.urls import path
from real_estate_web_application.properties_api import views

urlpatterns = [
    path('profile_api/', views.ProfileAPIView.as_view(), name='profile-api'),
    path('location_api/', views.LocationAPIView.as_view(), name='profile-api'),
    path('parking_api/', views.ParkingAPIView.as_view(), name='profile-api'),
    path('real_estate_api/', views.PropertiesAPIView.as_view(), name='real-estate-api'),

]