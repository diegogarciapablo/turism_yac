from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("probando primera vista en el index")
# Create your views here.
