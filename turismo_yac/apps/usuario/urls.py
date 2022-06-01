from django.urls import path

from .views import *

urlpatterns = [
    path('logout/',logout_request,name='logout'),
]