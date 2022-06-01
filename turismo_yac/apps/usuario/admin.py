from django.contrib import admin

from django.contrib.auth.models import Group
from .models import *
admin.site.register(Usuario)
admin.site.register(Genero)
admin.site.register(Rol)
admin.site.register(Pais)
admin.site.unregister(Group)
# Register your models here.
