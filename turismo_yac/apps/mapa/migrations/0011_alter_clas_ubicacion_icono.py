# Generated by Django 4.0.4 on 2023-03-15 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapa', '0010_alter_comentario_puntaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clas_ubicacion',
            name='icono',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='icono del marcador'),
        ),
    ]