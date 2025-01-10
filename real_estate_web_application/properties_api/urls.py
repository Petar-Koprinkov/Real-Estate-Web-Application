from django.urls import path, include
from real_estate_web_application.properties_api import views

urlpatterns = [
    path('user_api', include([
        path('', views.UserAPIView.as_view(), name='users-api'),
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
    path('real_estate_api/', views.PropertiesAPIView.as_view(), name='real-estate-api'),

]