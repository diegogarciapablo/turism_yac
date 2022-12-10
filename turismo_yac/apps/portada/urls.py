from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('admin_main', index_main, name='index_main'),
    path('historia', Historia, name='historia'),
]