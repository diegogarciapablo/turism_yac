from django.urls import path

from .views import *

urlpatterns = [
    path('prueba', prueba, name='prueba'),
    path('reg_paseov', reg_paseov, name='repaseov'),
    path('list_paseosv', Lista_paseosv, name='listaseov'),
    path('ver_paseo_v/<int:id>', VerPaseoV, name='verpaseov'),
]