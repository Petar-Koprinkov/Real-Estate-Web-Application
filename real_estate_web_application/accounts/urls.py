from django.contrib.auth.views import LogoutView
from django.urls import path, include
from real_estate_web_application.accounts import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('statistics/', views.StatisticView.as_view(), name='statistics'),
    path('profile/', include([
        path('<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail'),
        path('<int:pk>/edit/', views.ProfileEditView.as_view(), name='profile-edit'),
        path('<int:pk>/delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
    ])),
    # Url for Django REST
    path('', views.ProfileViewApi.as_view(), name='retrieve-profile-api'),

]
