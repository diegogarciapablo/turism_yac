# Generated by Django 4.0.4 on 2022-11-22 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapa', '0002_ubicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubicacion',
            name='clasificacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mapa.clas_ubicacion'),
        ),
    ]
