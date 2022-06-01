from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import logout, authenticate
# Create your views here.
def logout_request(request):
    logout(request)
    messages.info(request,"usted a cerrado sesion")
    return redirect('mapa:index')

def cambiar_contraseña(request):
    