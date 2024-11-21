from django.urls import path

from real_estate_web_application.real_estate import views

urlpatterns = [
    path('create_location', views.CreateLocationView.as_view(), name='create-location'),
    path('properties/', views.PropertyListView.as_view(), name='properties'),
]