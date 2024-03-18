from django.contrib import admin
from django.urls import path
from django.http import HttpResponse  # Import HttpResponse instead of HttpRequest
from . import views



urlpatterns = [

    path('', views.home, name='home'),
    path('generate_vin/', views.generate_vin, name='generate_vin'),
    path('vin_list/', views.vin_list, name='vin_list'),
]