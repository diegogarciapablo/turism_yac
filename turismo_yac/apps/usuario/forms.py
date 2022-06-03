from django import forms
from .models import Usuario

class FormularioUsuario(forms.ModelForm):
    #formulario para registro de usuarios
    password1 = forms.CharField(label = 'contraseña', widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'ingrese su contraseña',
            'id' : 'password1', 
            'required' : 'required',
        }
    ))

    password2 = forms.CharField(label = 'contraseña de verificacion', widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'confirme su contraseña',
            'id' : 'password2', 
            'required' : 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('username','genero','nacionalidad')
        widgets = {
            'username' : forms.EmailInput(
                attrs = {
                    'class' : 'validate'
                }
                ),
            'genero' : forms.TextInput(
                attrs = {
                    'class' : 'validate'
                }
                ),
            'nacionalidad' : forms.TextInput(
                attrs = {
                    'class' : 'validate'
                }
                )
        }