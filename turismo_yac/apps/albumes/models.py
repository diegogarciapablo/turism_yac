from django.db import models

# Create your models here.
class Album(models.Model):
    id = models.AutoField(primary_key = True)
    n_album = models.CharField(verbose_name = 'nombre del album', max_length=50, blank=True, null = True)

    def __str__(self):
        return f'{self.n_album}'
    class Meta:
        verbose_name = 'album'
        verbose_name_plural = 'albumes'
        ordering = ['id']

class Foto(models.Model):
    id = models.AutoField(primary_key = True)
    ruta_foto = models.FileField(upload_to='fotos/', blank=False, null= True)
    descripcion = models.CharField(verbose_name = 'descripcion', max_length=200, blank=True, null = True)
    album = models.ForeignKey('Album', on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f'{Album.n_album} {self.id}'
    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ['id']