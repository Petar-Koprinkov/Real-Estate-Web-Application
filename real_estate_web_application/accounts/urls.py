from django.urls import path

from real_estate_web_application.accounts import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
]