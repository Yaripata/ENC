# Generated by Django 5.0.6 on 2024-07-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_registroproduccion_codigo_combustible'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroAcciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.CharField(max_length=255)),
                ('accion', models.CharField(choices=[('MOD', 'Modificacion'), ('ELI', 'Eliminacion'), ('CRE', 'Creacion')], max_length=5)),
                ('registro', models.PositiveIntegerField()),
            ],
        ),
    ]
