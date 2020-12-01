from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('login', views.login, name='userlogin'),
    path('register', views.register, name='userregister'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='userdashboard'),
    path('donations', views.donations, name='userdonations'),
]
