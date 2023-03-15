from django.shortcuts import render, redirect
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


def index_main(request):
    if request.user.is_authenticated and request.user.rol_id == 1:
        list_clas=Clas_ubicacion.objects.all()
        context={
            'list_clas':list_clas,
                }
        return render(request, 'main_admin.html', context)
    else:
        messages.warning(request,f'solo un administrador puede ingresar a esa seccion')
        return redirect('portada:index')