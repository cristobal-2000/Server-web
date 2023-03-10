# Generated by Django 4.1.3 on 2022-11-25 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicApp', '0002_especialidades_medico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('nombres', models.CharField(max_length=50)),
                ('apellido_p', models.CharField(max_length=25)),
                ('apellido_m', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=25)),
                ('dateB', models.DateTimeField(blank=True, null=True)),
                ('address', models.CharField(max_length=25)),
                ('Comuna', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=25)),
                ('emergencyContact', models.CharField(max_length=25)),
                ('emergencyPhone', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=25)),
                ('health', models.CharField(max_length=25)),
            ],
        ),
    ]
