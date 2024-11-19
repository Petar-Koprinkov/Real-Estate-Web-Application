

from django.contrib.auth.views import LogoutView
from django.urls import path, include
from real_estate_web_application.accounts import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', include([
        path('<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    ])),

]