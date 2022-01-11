# Generated by Django 3.0.7 on 2021-12-13 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='autos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=40)),
                ('modelo', models.IntegerField()),
                ('tipo', models.CharField(max_length=40)),
                ('entregado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField()),
                ('carrera', models.CharField(max_length=40)),
                ('universidad', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='inmuebles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=40)),
                ('ciudad', models.CharField(max_length=40)),
                ('anio', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]