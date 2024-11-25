from django.urls import path, include
from real_estate_web_application.real_estate import views

urlpatterns = [
    path('create_location', views.CreateLocationView.as_view(), name='create-location'),
    path('create_parking', views.CreateParkingView.as_view(), name='create-parking'),
    path('properties/', views.PropertyListView.as_view(), name='properties'),
    path('add_property/', views.AddPropertyView.as_view(), name='add-property'),
    path('property/<int:pk>/', include([
        path('', views.DetailPropertyView.as_view(), name='detail-property'),
        path('edit/', views.EditPropertyView.as_view(), name='edit-property'),
        path('delete/', views.DeletePropertyView.as_view(), name='delete-property'),
    ]))
]