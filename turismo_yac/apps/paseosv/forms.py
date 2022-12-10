from django import forms
from .models import Paseo_v

class FormPaseoV(forms.ModelForm):
    class Meta:
        model = Paseo_v
        fields = ('url','ubicacion')
        widgets = {
            'url' : forms.TextInput(
                attrs = {
                    'class' : 'validate',
                }
                ),
            'ubicacion' : forms.Select(
                attrs = {'class' : 'validate',}),
        }