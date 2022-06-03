from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('listado_usuarios/',login_required(ListadoUsuario.as_view()),
        name = 'listar_usuarios')
    path('registrar_usuario/',RegistrarUsuario.as_view(),
        name = 'registrar_usuario')
]