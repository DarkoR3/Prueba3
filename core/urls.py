
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('services', services, name='services'),
    path('about', about, name='about'),
]
