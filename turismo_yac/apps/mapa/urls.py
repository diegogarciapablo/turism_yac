from django.urls import path

from .views import *

urlpatterns = [
    path('registrar_ubicacion/',RegistrarUbicacion, name = 'registro_ubi'),
    path('ver_map/',Mapa, name='vmapa'),
]