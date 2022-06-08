from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('registrar_usuario/',RegistrarUsuario, name = 'registrar_usuario'),
    path('listado_usuarios/',ListadoUsuario, name='listar_usuario'),
    path('editar_usuario/<int:id>',EditarUsuario, name = 'editar_autor'),
]