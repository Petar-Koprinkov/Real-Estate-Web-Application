from django.urls import path, include
from rest_framework.authtoken.views import ObtainAuthToken
from real_estate_web_application.properties_api import views

urlpatterns = [
    path('DRF-login', ObtainAuthToken.as_view(), name='DRF-login'),
    path('user_api', include([
        path('', views.UserAPIView.as_view(), name='users-api'),
        path('<int:pk>', views.UserListAPIViewSet.as_view(), name='user-list'),
    ])),
    path('profile_api/', include([
        path('',  views.ProfileAPIView.as_view(), name='profiles-api'),
        path('<int:pk>', views.ProfilesListAPIViewSet.as_view(), name='profile-list'),
    ])),
    path('location_api/', include([
        path('', views.LocationAPIView.as_view(), name='location-list'),
        path('<int:pk>', views.LocationListAPIViewSet.as_view(), name='location-api'),
    ])),
    path('parking_api/', include([
        path('', views.ParkingAPIView.as_view(), name='parking-list'),
        path('<int:pk>', views.ParkingAPIViewSet.as_view(), name='parking-api'),
    ])),
    path('real_estate_api/', include([
        path('', views.PropertiesAPIView.as_view(), name='real-estate-list'),
        path('<int:pk>', views.PropertiesAPIViewSet.as_view(), name='real-estate-api'),
    ])),

]