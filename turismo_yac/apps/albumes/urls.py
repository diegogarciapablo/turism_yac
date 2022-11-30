from django.urls import path

from .views import *

urlpatterns = [
    path('prueba', prueba, name='prueba'),
]