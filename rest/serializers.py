from rest_framework import serializers
from core.models import RegistroProduccion

class RegistroProduccionSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegistroProduccion
        fields = ('id','codigo_combustible','litros_producidos','fecha_produccion', 'turno', 'hora_registro', 'operador')
        read_only_fields = ('id','codigo_combustible','litros_producidos','fecha_produccion', 'turno', 'hora_registro', 'operador')

