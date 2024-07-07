from django.db import models

# Create your models here.

tipos_combustiles = [
    ("G93" , "Gasolina 93 Octanos"),
    ("G95" , "Gasolina 95 Octanos"),
    ("G97" , "Gasolina 97 Octanos"),
    ("DIE" , "Diesel convencional"),
    ("DIP" , "Diesel de alto rendimiento"),
    ("JA1" , "Jet A-1"),
    ("AVG" , "Av Gas"),
]

tipos_turnos = [
    ("AM" , "Mañana"),
    ("PM" , "Tarde"),
    ("MM" , "Noche"),
]

tipos_accion = [
    ("MOD" , "Modificacion"),
    ("ELI" , "Eliminacion"),
    ("CRE" , "Creacion")
]

class Plantas(models.Model):
    codigo_planta = models.CharField(max_length=4)
    nombre_planta = models.CharField(max_length=100)

    def __str__(self):
        return self.codigo_planta
    

class Combustibles(models.Model):
    codigo_combustible = models.CharField(max_length=4)
    nombre_combustible = models.CharField(max_length=60)
    zona_produccion = models.ForeignKey("Plantas", on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo_combustible
    

class RegistroProduccion(models.Model):
    codigo_combustible = models.ForeignKey("Combustibles", on_delete=models.CASCADE)
    litros_producidos = models.PositiveIntegerField()
    fecha_produccion = models.DateField()
    turno = models.CharField(max_length=4, choices=tipos_turnos)
    hora_registro = models.TimeField()
    operador = models.CharField(max_length=255)


class RegistroAcciones(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=255)
    accion = models.CharField(max_length=5, choices=tipos_accion)
    registro = models.PositiveIntegerField()