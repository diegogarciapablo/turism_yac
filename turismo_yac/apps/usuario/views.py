from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Usuario
from .forms import FormularioUsuario
# Create your views here.

class ListadoUsuario(ListView):
    model = Usuario
    template_name = 'usuario/listar_usuarios.html'
    def get_queryset(self):
        return self.model.objects.filter(is_active=True)

class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuario/crear_usuario.html'
    success_url = reverse_lazy('main_usuario.html')

    