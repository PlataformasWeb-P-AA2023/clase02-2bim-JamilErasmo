# Generated by Django 4.2.2 on 2023-06-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0002_estudiante_tipo_estudiante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='edad',
            field=models.IntegerField(verbose_name='edad de estudiante'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='Nombre de estudiante'),
        ),
    ]
