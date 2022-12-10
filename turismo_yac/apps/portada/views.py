from django.shortcuts import render 
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from apps.mapa.models import *


def index(request):
    list_clas=Clas_ubicacion.objects.all()
    context={
        'list_clas':list_clas,
            }
    return render(request, 'main_usuario.html', context)

def Historia(request):
        return render(request, 'pruebas/historia.html')

@login_required
def index_main(request):
    list_clas=Clas_ubicacion.objects.all()
    context={
        'list_clas':list_clas,
            }
    if request.user.rol_id == 1:
        return render(request, 'main_admin.html', context)
    else:
         messages.info(request,f'usted no tiene autorizacion para ingresar a este sitio')
    return render(request, 'main_usuario.html', context)