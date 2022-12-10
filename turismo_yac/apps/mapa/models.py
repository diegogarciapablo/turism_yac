from django.db import models
class Clas_ubicacion(models.Model):
    id = models.AutoField(primary_key = True)
    n_clas = models.CharField(verbose_name = 'clasificacion de ubicacion', max_length=50, unique = True, blank=True, null = True)
    color = models.CharField(verbose_name = 'color del marcador', max_length=50, unique = True, blank=True, null = True)
    icono = models.CharField(verbose_name = 'icono del marcador', max_length=50, unique = True, blank=True, null = True)

    def __str__(self):
        return f'{self.n_clas}'
    class Meta:
        verbose_name = 'clasificacion'
        verbose_name_plural = 'clasificaciones'
        ordering = ['id']

class Ubicacion(models.Model):
    id = models.AutoField(primary_key = True)
    n_ubicacion = models.CharField(verbose_name = 'nombre de ubicacion', max_length=50, unique = True, blank=True, null = True)
    clasificacion = models.ForeignKey('Clas_ubicacion', on_delete=models.CASCADE, default=1)
    direccion = models.CharField(verbose_name = 'direccion', max_length=100, blank=True, null = True)
    latitud = models.CharField(verbose_name = 'latitud', max_length=50, blank=True, null = True)
    longitud = models.CharField(verbose_name = 'longitud', max_length=50,  blank=True, null = True)
    descripcion = models.CharField(verbose_name = 'descripcion', max_length=255,  blank=True, null = True)
    estado = models.BooleanField(verbose_name = 'estado',default=False)
    autorizacion = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, null = True)
    
    def __verbose__(id):
        return self.n_ubicacion
    def __str__(self):
        return f'{self.n_ubicacion}'
    class Meta:
        verbose_name = 'ubicacion'
        verbose_name_plural = 'ubicaciones'
        ordering = ['id']


class Comentario(models.Model):
    puntaje_choices=(
        ('1','MALO'),
        ('2','MODESTO'),
        ('3','COMUN'),
        ('4','BUENO'),
        ('5','PERFECTO'),
            )
    id = models.AutoField(primary_key= True)
    texto = models.CharField(verbose_name = 'comentario', max_length=150, blank=True, null = True)
    ubicacion = models.ForeignKey('Ubicacion', on_delete=models.CASCADE,default=1)
    autor = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    puntaje = models.CharField(verbose_name = 'puntaje', max_length=1, blank=True, null = True, choices=puntaje_choices, default=3)