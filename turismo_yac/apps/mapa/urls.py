from django.urls import path

from .views import *

urlpatterns = [
    path('registrar_ubicacion/',RegistrarUbicacion, name = 'registro_ubi'),
    path('editar_ubicacion/<int:id>',EditarUbicacion, name = 'edit_ubi'),
    path('ver_map/',Mapa, name='vmapa'),
    path('listar_ubis/',Listaubi1, name='listubi'),
    path('list_filt_ubis/<int:id>',Listaubi2, name='listubif'),
    path('reg_coment_ubi/<int:ubi>',RegComentUbi, name='Regcomentubi'),
    path('reg_clas_ubi',reg_clas, name='regclas'),
    path('edit_clas_ubi/<int:id>',Editar_clas, name='editclas'),
    path('listar_clas/',List_Clas, name='listclas'),
    path('reg_comentario/',Reg_Comentario, name='recoment'),
    path('edit_comentario/<int:id>',Editar_coment, name='editcoment'),
    path('list_coment/',List_Comentarios, name='listcoments'),
    path('mis_coment/<int:id>',List_Comentarios2, name='miscoments'),
]