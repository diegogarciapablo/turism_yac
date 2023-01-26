from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def iniciosesion(request):
    if request.method == 'POST':
        form_log = FormLog(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            messages.info(request,f'bienvenido {request.user.nombres} {request.user.apellidos}')
            return redirect('portada:index')
        else:
            messages.error(request,f'correo o contraseña invalidos')
    else:
        print("llego a get")
        form_log = FormLog()
    context = {
        'form':form_log
        }
    return render(request,'registration/login.html', context)


def RegistrarUsuario(request):
    if request.method == 'POST':
        form = FormularioUsuario(request.POST)
        if form.is_valid():
            usuario = form.save()
            return redirect('portada:index')
        else:
            for error in form.errors.values():
                messages.error(request,f'{error}')
    else:
        form = FormularioUsuario()
    context = {
        'form':form
        }
    return render(request,'usuario/crear_usuario.html', context)

def ListadoUsuario(request):
    if request.user.rol_id == 1:
        u_lista = Usuario.objects.all()
        return render(request,'usuario/listar_usuarios.html',{'u_lista': u_lista})
    else:
        return redirect('portada:index')


def EditarUsuario(request,id):
    if request.user.id==id:
        usuario = Usuario.objects.get(id=id)
        if request.method == 'GET':
            u_form = FormEditUsuario(instance = usuario)
        else:
            u_form = FormEditUsuario(request.POST, instance = usuario)
            if u_form.is_valid():
                print("usuario valido")
                u_form.save()
            return redirect('portada:index')
        print(u_form)
        return render(request,'usuario/editar_usuario.html',{'u_form':u_form})
    else:
        return redirect('portada:index')

def AdminEditaUsuario(request,id):
    if request.user.rol_id == 1:
        usuario = Usuario.objects.get(id=id)
        if request.method == 'GET':
           u_form = FormEditAdmin(instance = usuario)
        else:
            u_form = FormEditAdmin(request.POST, instance = usuario)
            if u_form.is_valid():
                print("usuario valido")
                u_form.save()
            return redirect('portada:index')
        return render(request,'usuario/admin_edita_usuario.html',{'u_form':u_form})
    else:
        return redirect('portada:index')
