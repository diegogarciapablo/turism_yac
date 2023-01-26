from django.db import IntegrityError, transaction
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import authenticate

from django.http.response import HttpResponse
from .forms import *
from .models import *
from django.conf import settings
import ntpath
import mimetypes
import os

from django.core.exceptions import ObjectDoesNotExist

def prueba(request):
    return render(request, 'galeria/galeria.html')

def CE_Album(request):
    if request.method == 'POST':
        form = FormAlbum(request.POST)
        form_valid= form.is_valid()
        if form_valid:
            form.save()
            messages.info(request,f'registro exitoso de album')
            return redirect('portada:index')
        else:
            for error in form.errors.values():
                messages.error(request,f'{error}')
    else:
        form=FormAlbum()
    context={
        'form':form,
            }
    return render(request,'galeria/r_e_album.html', context)

def Listar_Album(request):
        a_lista = Album.objects.all()
        return render(request,'galeria/listar_albumes.html',{'a_lista': a_lista})


def Editar_Album(request,id):
    album = Album.objects.get(id=id)
    if request.method == 'GET':
        form = FormAlbum(instance = album)
    else:
        print('llega a post de edicion')
        form = FormAlbum(request.POST, instance = album)
        nalbum = request.POST.get('n_album')
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.info(request,f'modificacion exitosa de album {nalbum}')
            return redirect('portada:index')
        else: 
            for error in form.errors.values():
                messages.error(request,f'{error}')
    return render(request,'galeria/r_e_album.html',{'form':form})

def R_Foto(request):
    if request.method == 'POST':
        form = FormFoto(request.POST, request.FILES)
        print('llega a post de creacion foto')
        if form.is_valid():
            print('paso validacion foto')
            form.save()
            messages.info(request,f'registro exitoso de album')
            return redirect('portada:index_main')
        else:
            print(form.errors)
            for error in form.errors.values():
                messages.error(request,f'{error}')
    else:
        form=FormFoto()
    context={
        'form':form,
            }
    return render(request,'galeria/re_foto.html', context)

def Listar_Archivos(request,id):
        f_lista = Foto.objects.filter(album=id)
        return render(request,'galeria/list_foto.html',{'f_lista': f_lista})

def descargar_archivo(request, id): 
    archivo = Foto.objects.get(id=id)
    filepath1 = str(settings.BASE_DIR)
    filepath2 = str(archivo.ruta_foto)
    fullpath = filepath1 +'/media/'+filepath2
    path = open(fullpath, errors="ignore") 
    mime_type, _ = mimetypes.guess_type(fullpath)
    response = HttpResponse(path, content_type = mime_type)
    filename = ntpath.basename(str(archivo.ruta_foto))
    response['Content-Disposition'] = f"attachment; filename={filename}"
    return response

def Elim_Foto(request, id):
    foto = Foto.objects.get(id=id)
    foto.delete()
    messages.warning(request,f'foto eliminada con exito')
    return redirect('album:listalbum')

def Listar_Fotos(request, id):
        f_lista = Foto.objects.filter(album=id)
        return render(request,'galeria/vis_fotos.html',{'f_lista': f_lista})