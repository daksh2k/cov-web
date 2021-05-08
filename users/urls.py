from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('login', views.login, name='userlogin'),
    path('register', views.register, name='userregister'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='userdashboard'),
    path('viewrequirement/<int:requirement_id>', views.viewrequirement, name='viewrequirement'),
    path('viewdonation/<int:donation_id>', views.viewdonation, name='viewdonation'),
    path('donate/<int:requirement_id>', views.DonateView.as_view(), name='donate'),
    path('donations', views.donations, name='userdonations'),
]
