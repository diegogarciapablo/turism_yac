from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, username,  password = None):
        if not username:
            raise ValueError("debes escribir un nombre de usuario")
        if not password:
            raise ValueError("debes escribir tu contraseña")
        usuario = self.model(
            username = self.normalize_email(username),
            
        )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, password):
        usuario = self.create_user(
            username,
            password=password
            )

        usuario.u_admin = True
        usuario.save()
        return usuario

# Create your models here.
class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.EmailField(verbose_name = 'email del usuario', unique = True, max_length=150, blank=False, null= True)
    nombres = models.CharField('nombres', max_length=150, blank=False, null = True)
    apellidos = models.CharField('apellidos', max_length=150, blank=False, null = True)
    rol = models.ForeignKey('Rol', on_delete=models.CASCADE, default=2)
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE, default=1)
    nacionalidad = models.ForeignKey('Pais', on_delete=models.CASCADE,default=1)
    estado = models.BooleanField(default=True)
    u_admin = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.apellidos}, {self.nombres}'
    def has_perm(self,perm,obj = None):
        return True
    def has_module_perms(self,app_label):
        return True

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        ordering = ['id']

    @property
    def is_staff(self):
        return self.u_admin
    
class Rol(models.Model):
    id = models.AutoField(primary_key = True)
    n_rol = models.CharField('rol',max_length=50, unique = True, blank=True, null = True)

    def __str__(self):
        return f'{self.n_rol}'
    class Meta:
        verbose_name = 'rol'
        verbose_name_plural = 'roles'
        ordering = ['id']

class Genero(models.Model):
    id = models.AutoField(primary_key = True)
    n_gen = models.CharField('genero',max_length=50, unique = True, blank=True, null = True)

    def __str__(self):
        return f'{self.n_gen}'
    class Meta:
        verbose_name = 'genero'
        verbose_name_plural = 'generos'
        ordering = ['id']

class Pais(models.Model):
    id = models.AutoField(primary_key = True)
    n_pais = models.CharField('pais de origen', max_length=50, unique = True, blank=True, null = True)

    def __str__(self):
        return f'{self.n_pais}'
    class Meta:
        verbose_name = 'pais de origen'
        verbose_name_plural = 'paises de origen'
        ordering = ['id']