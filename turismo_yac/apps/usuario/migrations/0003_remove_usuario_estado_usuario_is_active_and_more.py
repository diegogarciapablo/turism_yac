# Generated by Django 4.0.4 on 2022-06-02 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_alter_usuario_genero_alter_usuario_nacionalidad_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='estado',
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='estado'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='u_admin',
            field=models.BooleanField(default=False, verbose_name='administrador'),
        ),
    ]
