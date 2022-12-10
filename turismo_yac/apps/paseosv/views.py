from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from .forms import *
from .models import *


def prueba(request):
    return render(request, 'paseosv/paseo_v.html')

def reg_paseov(request):
    if request.method == 'POST':
        form = FormPaseoV(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,f'registro exitoso de paseo_v')
            return redirect('portada:index')
        else:
            print(form.errors)
            for error in form.errors.values():
                messages.error(request,f'{error}')
    else:
        form=FormPaseoV()
    context={
        'form':form,
            }
    return render(request,'paseosv/repaseov.html', context)

def Lista_paseosv(request):
    p_lista = Paseo_v.objects.all()
    context={
    'p_lista': p_lista,
        }
    return render(request,'paseosv/list_paseos_v.html', context)

def VerPaseoV(request,id):
    control_paseo = Paseo_v.objects.all().values_list()
    confirm = False
    for control in control_paseo:
        if control[0] == id:
            confirm = True
    if confirm:
        paseo=Paseo_v.objects.get(id=id)
        return render(request, 'paseosv/paseo_v.html',{'paseo':paseo,})
    else:
        messages.info(request,f'estas intentando ingresar a un paso invalido')
        return redirect('paseov:listaseov')

    