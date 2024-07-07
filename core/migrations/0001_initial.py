# Generated by Django 4.2.11 on 2024-07-03 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroProduccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_combustible', models.CharField(choices=[('G93', 'Gasolina 93 Octanos'), ('G95', 'Gasolina 95 Octanos'), ('G97', 'Gasolina 97 Octanos'), ('DIE', 'Diesel convencional'), ('DIP', 'Diesel de alto rendimiento'), ('JA1', 'Jet A-1'), ('AVG', 'Av Gas')], max_length=4)),
                ('litros_producidos', models.PositiveIntegerField()),
                ('fecha_produccion', models.DateField()),
                ('turno', models.CharField(choices=[('AM', 'Mañana'), ('PM', 'Tarde'), ('MM', 'Noche')], max_length=4)),
                ('hora_registro', models.TimeField()),
                ('operador', models.CharField(max_length=255)),
            ],
        ),
    ]
