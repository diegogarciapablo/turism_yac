"""turismo_yac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from apps.mapa import views
from apps.usuario import views
from apps.portada import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.portada.urls','portada'))),
    path('mapa/', include(('apps.mapa.urls','mapa'))),
    path('usuarios/', include(('apps.usuario.urls','usuarios'))),
    path('cuentas/', include('django.contrib.auth.urls')),
    path('album/', include(('apps.albumes.urls','album'))),
    path('paseos_v/', include(('apps.paseosv.urls','paseov'))),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)