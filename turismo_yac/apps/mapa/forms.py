from django import forms
from .models import *

class FormUbicacion(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ('clasificacion','n_ubicacion','direccion','latitud','longitud','descripcion','autorizacion','estado')
        widgets = {
            'clasificacion' : forms.Select(
                attrs = {
                    'class' : 'validate',
                }
                ),
            'n_ubicacion' : forms.TextInput(
                attrs = {
                    'class' : 'validate',
                    'required' : 'required',
                }
                ),
            
            'direccion' : forms.TextInput(
                attrs = {
                    'class' : 'validate',
                }
                ),
            'latitud' : forms.TextInput(
                attrs = {
                    'class' : 'validate',
                    'required' : 'required',
                }
                ),
            'longitud' : forms.TextInput(
                attrs = {
                    'class' : 'validate',
                    'required' : 'required',
                }
                ),
            'descripcion' : forms.Textarea(
                attrs = {
                    'class' : 'validate'
                }
                ),
            'autorizacion' : forms.TextInput(
                attrs = {
                    'class' : 'validate'
                }
                ),
            'estado' : forms.CheckboxInput(
                attrs = {
                    'class' : 'validate'
                }
                ),
        }

class FormClasUbicacion(forms.ModelForm):
    class Meta:
        model = Clas_ubicacion
        fields = ('n_clas','color','icono')
        widgets = {
            'n_clas' : forms.TextInput(
                attrs = {
                    'class' : 'validate',
                }
                ),
            'color' : forms.TextInput(
                attrs = {
                    'class' : 'validate',
                }
                ),
            'icono' : forms.TextInput(
                attrs = {
                    'class' : 'validate',
                }
                ),
        }

class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('texto','ubicacion','autor','puntaje')
        widgets = {
            'texto' : forms.Textarea(
                attrs = {
                    'class' : 'validate',
                }
                ),
            'ubicacion' : forms.Select(
                attrs = {
                    'class' : 'validate'
                }
                ),
            'autor' : forms.TextInput(
                attrs = {
                    'class' : 'validate'
                }
                ),
            'puntaje' : forms.TextInput(
                attrs = {
                    'class' : 'validate'
                }
                ),
            }