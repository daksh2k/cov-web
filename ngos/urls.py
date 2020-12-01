from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('login', views.login, name='ngologin'),
    path('register', views.register, name='ngoregister'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='ngodashboard'),
    path('requirements', views.requirements, name='ngorequirements'),
]
