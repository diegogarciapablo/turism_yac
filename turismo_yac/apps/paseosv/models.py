from django.db import models

# Create your models here.
class Paseo_v(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=512, verbose_name= 'url', null=False, blank=False, help_text="ingrese la url")
    ubicacion = models.OneToOneField('mapa.Ubicacion', on_delete=models.CASCADE, blank=False, unique=True, default=5)

    def __str__(self):
        return self.mapa.ubicacion.n_ubicacion

    class Meta:
        verbose_name = 'paseo virtual'
        verbose_name_plural = 'paseos virtuales'
        ordering = ['id']

