from django.urls import path
from .views import home, add_vin_to_database

urlpatterns = [
    path('', home, name='home'),
    path('add_vin/', add_vin_to_database, name='add_vin'),
]