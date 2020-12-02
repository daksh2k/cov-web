from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('login', views.login, name='ngologin'),
    path('register', views.register, name='ngoregister'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='ngodashboard'),
    path('requirements', views.requirements, name='ngorequirements'),
    path('requirements/<int:requirement_id>', views.removerequirements, name='removerequirements'),
    path('viewdonation/<int:donation_id>', views.viewdonationngo, name='viewdonationngo'),
    path('acceptdonation/<int:donation_id>', views.acceptdonation, name='acceptdonation'),
]
