# Generated by Django 3.0.7 on 2021-05-08 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('codigo', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('duracion', models.PositiveSmallIntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('creditos', models.PositiveSmallIntegerField()),
                ('docente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='estudiante',
            fields=[
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('apellido_paterno', models.CharField(max_length=35)),
                ('apellido_materno', models.CharField(max_length=35)),
                ('nombres', models.CharField(max_length=35)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('vigencia', models.BooleanField(default=True)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academica.Carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_matricula', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academica.Curso')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academica.estudiante')),
            ],
        ),
    ]
