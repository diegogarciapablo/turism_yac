# Generated by Django 4.0.4 on 2022-12-05 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('n_album', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='nombre del album')),
            ],
            options={
                'verbose_name': 'album',
                'verbose_name_plural': 'albumes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ruta_foto', models.FileField(upload_to='fotos/')),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True, verbose_name='nombre del album')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
                'ordering': ['id'],
            },
        ),
    ]
