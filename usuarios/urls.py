from re import template
from telnetlib import LOGOUT
from urllib.parse import urlparse
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(
        template_name ='login.html'
        ), name="login"),
    
    path('logout/',auth_views.LogoutView.as_view(),name="logout")
]
