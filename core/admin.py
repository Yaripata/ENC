from django.contrib import admin
from .models import RegistroProduccion, Combustibles, Plantas, RegistroAcciones
# Register your models here.

@admin.register(RegistroProduccion)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('id','fecha_produccion', 'hora_registro', 'operador', 'turno', 'codigo_combustible', 'litros_producidos')

@admin.register(Plantas)
class PlantasAdmin(admin.ModelAdmin):
    list_display = ('nombre_planta', 'codigo_planta')

@admin.register(Combustibles)
class CombustiblesAdmin(admin.ModelAdmin):
    list_display = ('nombre_combustible', 'codigo_combustible', 'zona_produccion')

@admin.register(RegistroAcciones)
class RegistroAccionesAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'usuario', 'accion', 'registro')