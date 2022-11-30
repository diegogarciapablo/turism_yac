from django import forms
from .models import Ubicacion

class FormUbicacion(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ('clasificacion','n_ubicacion','direccion','latitud','longitud','descripcion','autorizacion')
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
        }