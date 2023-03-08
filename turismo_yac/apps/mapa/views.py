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

@login_required
def RegistrarUbicacion(request):
    if request.method == 'POST':
        ubicacion_form = FormUbicacion(request.POST)
        ubi_valid= ubicacion_form.is_valid()
        nubi = request.POST.get('n_ubicacion')
        if ubi_valid:
            ubicacion_form.save()
            messages.info(request,f'registro exitoso de ubicacion {nubi}')
            return redirect('portada:index')
        else:
            for error in ubicacion_form.errors.values():
                messages.error(request,f'{error}')
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


@login_required
def EditarUbicacion(request,id):
    ubi = Ubicacion.objects.get(id=id)
    if request.method == 'GET':
        ubi_form = FormUbicacion(instance = ubi)
    else:
        ubi_form = FormUbicacion(request.POST, instance = ubi)
        nubi = request.POST.get('n_ubicacion')
        if ubi_form.is_valid():
            ubi_form.save()
            messages.info(request,f'modificacion exitosa de categoria {nubi}')
            return redirect('portada:index')
        else: 
            for error in ubi_form.errors.values():
                messages.error(request,f'{error}')
    
    m = folium.Map(location=[ubi.latitud, ubi.longitud], zoom_start=16, )
    folium.Marker([ubi.latitud, ubi.longitud]).add_to(m)
    # obtencion de coordenadas
    m.add_child(folium.LatLngPopup())
    # representacion html del mapa
    m = m._repr_html_()
    context={
        'm': m,
        'ubi_form':ubi_form,
            }
    return render(request,'mapa/crear_ubi.html', context)

def Mapa(request):
    #obteniendo datos de la db
    ubi_lista = Ubicacion.objects.filter(estado=True).values_list()
    clas_lista = Clas_ubicacion.objects.all().values_list()
    #creando mapa
    m = folium.Map(location=[-22.01392810529076, -63.677741626018076], zoom_start=16, tiles='cartodbpositron',)
    #combinando ambas consultas
 
    for y in ubi_lista:
        for x in clas_lista:
            if x[0]==y[2]:
                html = "<b>"+x[1].upper()+"</br>"+y[1].upper()+"</b></br>"+y[3].upper()+"</br>"+"<a href=http://localhost:8000/mapa/reg_coment_ubi/"+str(x[0])+" Target='_top'><button>COMENTA</button></a>"
                iframe1 = branca.element.IFrame(html=html,width=170,height=130)
                v_icon=folium.Icon(color=x[2],icon=x[3])
                folium.Marker(location=[y[4],y[5]], popup=folium.Popup(iframe1, max_width=300),icon =v_icon ).add_to(m)
                    
    # representacion html del mapa
    m = m._repr_html_()
    context={
        'm': m,
            }
    return render(request, 'mapa/mapa.html', context)


def Listaubi1(request):
    if request.user.is_authenticated:
        u_lista = Ubicacion.objects.all()
        context={
        'u_lista': u_lista,
            }
        return render(request,'mapa/listarubi.html', context)
    else:
        messages.info(request,f'inicia sesion para ver esta opcion')
        return redirect('portada:index')
def Listaubi2(request, id):
    u_lista = Ubicacion.objects.filter(clasificacion=id,estado=True)
    punt=[]
    for u in u_lista:
        a=prom_star(u.id)
        punt.append([u.id,a])
    context={
    'punt':punt,
    'u_lista': u_lista,
        }
    return render(request,'mapa/listarubi.html', context)

def prom_star(x):
    cont=Comentario.objects.filter(ubicacion=x).count()
    if cont!=0:
        list_coment=Comentario.objects.filter(ubicacion=x)
        total=0
        prom=0
        for c in list_coment:
            total=total+c.puntaje
        prom=total/cont
        return (prom)
    else:
        return (0)



def reg_clas(request):
    if request.method == 'POST':
        form = FormClasUbicacion(request.POST)
        form_valid= form.is_valid()
        if form_valid:
            form.save()
            messages.info(request,f'registro exitoso de clasificacion de ubicacion')
            return redirect('portada:index')
        else:
            for error in form.errors.values():
                messages.error(request,f'{error}')
    else:
        form=FormClasUbicacion()
    context={
        'form':form,
            }
    return render(request,'mapa/re_cat_ubi.html', context)

def Editar_clas(request,id):
    clas = Clas_ubicacion.objects.get(id=id)
    if request.method == 'GET':
        form = FormClasUbicacion(instance = clas)
    else:
        form = FormClasUbicacion(request.POST, instance = clas)
        nclas = request.POST.get('n_clas')
        if form.is_valid():
            form.save()
            messages.info(request,f'modificacion exitosa de categoria {nclas}')
            return redirect('portada:index')
        else: 
            for error in form.errors.values():
                messages.error(request,f'{error}')
    return render(request,'mapa/re_cat_ubi.html',{'form':form})

@login_required
def List_Clas(request):
    c_lista = Clas_ubicacion.objects.all()
    context={
    'c_lista': c_lista,
        }
    return render(request,'mapa/listarclas.html', context)

def Reg_Comentario(request):
    if request.method == 'POST':
        form = FormComentario(request.POST)
        form_valid= form.is_valid()
        if form_valid:
            form.save()
            messages.info(request,f'registro exitoso del comentario')
            return redirect('portada:index')
        else:
            for error in form.errors.values():
                messages.error(request,f'{error}')
    else:
        form=FormComentario()
    context={
        'form':form,
            }
    return render(request,'mapa/re_comentario.html', context)

def Editar_coment(request,id):
    coment = Comentario.objects.get(id=id)
    if request.method == 'GET':
        form = FormComentario(instance = coment)
    else:
        form = FormComentario(request.POST, instance = coment)
        if form.is_valid():
            form.save()
            messages.info(request,f'modificacion exitosa de coemntario')
            return redirect('portada:index')
        else: 
            for error in form.errors.values():
                messages.error(request,f'{error}')
    return render(request,'mapa/re_comentario.html',{'form':form})

@login_required
def List_Comentarios(request):
    if request.user.rol_id == 1:
        c_lista = Comentario.objects.all()
        context={
        'c_lista': c_lista,
            }
        return render(request,'mapa/list_coment.html', context)
    else:
        messages.info(request,f'usted no tiene autorizacion para ingresar a este sitio')
    return redirect('portada:index')

@login_required
def List_Comentarios2(request,id):
    c_lista = Comentario.objects.filter(autor=id)
    context={
    'c_lista': c_lista,
        }
    return render(request,'mapa/list_coment.html', context)



@login_required
def RegComentUbi(request,ubi):
    if request.method == 'POST':
        form = FormComentario(request.POST)
        form_valid= form.is_valid()
        if form_valid:
            form.save()
            messages.info(request,f'registro exitoso del comentario')
            return redirect('portada:index')
        else:
            for error in form.errors.values():
                messages.error(request,f'{error}')
    else:
        form=FormComentario()
    context={
        'ubi':ubi,
        'form':form,
            }
    return render(request,'mapa/re_comentario.html', context)