from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate
def prueba(request):
    return render(request, 'paseosv/paseo_v.html')