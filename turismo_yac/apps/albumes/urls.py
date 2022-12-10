from django.urls import path
from .views import *
from apps.albumes import views
urlpatterns = [
    path('prueba', prueba, name='prueba'),
    path('CE_Album', CE_Album, name='CEAL'),
    path('Listar_Album', Listar_Album, name='listalbum'),
    path('Editar_Album/<int:id>', Editar_Album, name='edalbum'),
    path('R_Foto', R_Foto, name='RFOTO'),
    path('Listar_Foto/<int:id>', Listar_Archivos, name='listfoto'),
    path('descargar/<int:id>', views.descargar_archivo, name = "descargar"),
    path('Listar_Fotos/<int:id>', Listar_Fotos, name='listfotos'),
    path('Eliminar_Foto/<int:id>', Elim_Foto, name='elimfoto'),
]