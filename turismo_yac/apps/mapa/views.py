from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
import folium
import branca

def RegistrarUbicacion(request):
    if request.method == 'POST':
        print('llego a post')
        ubicacion_form = FormUbicacion(request.POST)
        print(ubicacion_form)
        ubi_valid= ubicacion_form.is_valid()
        print(ubi_valid)
        if ubi_valid:
            print('paso validacion')
            ubicacion_form.save()
            return redirect('portada:index')
    else:
        ubicacion_form=FormUbicacion()
        #creando mapa
    m = folium.Map(location=[-22.01392810529076, -63.677741626018076], zoom_start=16, )
    # obtencion de coordenadas
    m.add_child(folium.LatLngPopup())
    # representacion html del mapa
    m = m._repr_html_()
    context={
        'm': m,
        'ubi_form':ubicacion_form,
            }
    return render(request,'mapa/crear_ubi.html', context)


def Mapa(request):
    #obteniendo datos de la db
    ubi_lista = Ubicacion.objects.all().values_list()
    clas_lista = Clas_ubicacion.objects.all().values_list()
    
    grupo_plaza=folium.FeatureGroup(name='plazas')
    grupo_comidas=folium.FeatureGroup(name='e. comidas')
    grupo_alojamiento=folium.FeatureGroup(name='alojamientos')
    #llenando Iframe

    #creando mapa
    m = folium.Map(location=[-22.01392810529076, -63.677741626018076], zoom_start=16, tiles='cartodbpositron',)
    #marcadores y estableciendo capas
    for x in ubi_lista:
        for y in clas_lista:
            grupo_clas=folium.FeatureGroup(name=y[1])
            if x[2]==y[0]:
                html = "<b>"+y[1].upper()+"</br>"+x[1].upper()+"</b></br>"+x[3].upper()
                iframe1 = branca.element.IFrame(html=html,width=170,height=130)
                if x[2]==1:
                    v_icon=folium.Icon(color='green',icon='tree-conifer')
                    feature_g=grupo_plaza
                if x[2]==3:
                    v_icon=folium.Icon(color='orange',icon='cutlery')
                    feature_g=grupo_comidas
                if x[2]==2:
                    v_icon=folium.Icon(color='blue',icon='home')
                    feature_g=grupo_alojamiento
                folium.Marker(location=[x[4],x[5]], popup=folium.Popup(iframe1, max_width=300),icon =v_icon ).add_to(feature_g)

    #agregando capas y control de capas
    m.add_child(grupo_plaza)
    m.add_child(grupo_comidas)
    m.add_child(grupo_alojamiento)
    m.add_child(folium.map.LayerControl())
    # representacion html del mapa
    m = m._repr_html_()
    context={
        'm': m,
            }
    return render(request, 'mapa/mapa.html', context)