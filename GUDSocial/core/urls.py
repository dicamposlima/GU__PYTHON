"""Core URL Configuration"""
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import LoginView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social'))
]
