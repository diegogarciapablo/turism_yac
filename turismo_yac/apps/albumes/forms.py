from django import forms
from .models import *

class FormAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = ("n_album",)
        widgets = {
            'n_album' : forms.TextInput(
                attrs = {
                    'class' : 'validate',
                }
                ),
        }
    def clean_n_album(self):
        n_album = self.cleaned_data['n_album']
        if Album.objects.filter(n_album=n_album).exists():
            raise forms.ValidationError("este nombre de album esta en uso")
        return n_album

class FormFoto(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ('ruta_foto','descripcion','album')
        widgets = {
            'descripcion' : forms.TextInput(
                attrs = {
                    'class' : 'validate',

                }
                ),
            'album' : forms.Select(
                attrs = {
                    'class' : 'validate',
                }
                ),
        }