from django.urls import path

from real_estate_web_application.common import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]