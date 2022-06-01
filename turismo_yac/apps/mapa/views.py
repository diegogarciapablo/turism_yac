from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate
def index(request):
    if request.user.is_authenticated:
        messages.info(request,f'bienvenido{request.user.username}')
        return render(request, 'main_usuario.html')
    else:
        return render(request, 'main_usuario.html')
# Create your views here.
