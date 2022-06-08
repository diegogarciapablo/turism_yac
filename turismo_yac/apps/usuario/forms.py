from django import forms
from .models import Usuario

class FormularioUsuario(forms.ModelForm):
    #formulario para registro de usuarios
    password1 = forms.CharField(label = 'contraseña', widget = forms.PasswordInput(
        attrs = {
            'class' : 'validate',
            'id' : 'password1',
            'required' : 'required',
        }
    ))
    password2 = forms.CharField(label = 'confirme su contraseña', widget = forms.PasswordInput(
        attrs = {
            'class' : 'validate',
            'id' : 'password2',
            'required' : 'required',
        }
    ))
    class Meta:
        model = Usuario
        fields = ('username','nacionalidad','genero')
        widgets = {
            'username' : forms.EmailInput(
                attrs = {
                    'class' : 'validate',
                    'required' : 'required',
                }
                ),
            'nacionalidad' : forms.Select(
                attrs = {
                    'class' : 'validate'
                }
                ),
            'genero' : forms.TextInput(
                attrs = {
                    'class' : 'validate'
                }
                )
        }
    def clean_password2(self):
        """
        aqui se validara q ambas contraseñas del formulari coincidan
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("las contraseñas no coinciden")
        return password2
    def save(self, commit=True):
        # se redefine save para q guarde la contraseña tambien
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user

class FormEditUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username','nombres','apellidos','genero','nacionalidad')
        widgets = {
            'username' : forms.EmailInput(
                attrs = {
                    'class' : 'validate',
                    'required' : 'required',
                }
                ),
            'nombres' : forms.TextInput(
                attrs = {
                    'class' : 'validate',
                    'required' : 'required',
                }
                ),
            'apellidos' : forms.TextInput(
                attrs = {
                    'class' : 'validate',
                    'required' : 'required',
                }
                ),
            'genero' : forms.TextInput(
                attrs = {
                    'class' : 'validate'
                }
                ),
            'nacionalidad' : forms.Select(
                attrs = {
                    'class' : 'validate'
                }
                ),
        }

class FormEditAdmin(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('is_active','rol')
        widgets = {
            'is_active' : forms.CheckboxInput(
                attrs = {
                    'class' : 'validate',
                    'required' : 'required',
                }
                ),
            'rol' : forms.Select(
                attrs = {
                    'class' : 'validate'
                }
                ),
            }
