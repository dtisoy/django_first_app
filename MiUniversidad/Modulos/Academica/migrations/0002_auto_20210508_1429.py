# Generated by Django 3.0.7 on 2021-05-08 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academica.Estudiante'),
        ),
    ]
