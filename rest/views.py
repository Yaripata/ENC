from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import RegistroProduccion
from .serializers import RegistroProduccionSerializers
import datetime

class RegistroDetalle(APIView):
    def get(self, request, format=None):
        plantas = {}
        lista_registro = RegistroProduccion.objects.all()
        for reg in lista_registro:
            if reg.codigo_combustible.zona_produccion.codigo_planta not in plantas:
                plantas[reg.codigo_combustible.zona_produccion.codigo_planta] = {}
            if reg.codigo_combustible.codigo_combustible not in plantas[reg.codigo_combustible.zona_produccion.codigo_planta]:
                plantas[reg.codigo_combustible.zona_produccion.codigo_planta][reg.codigo_combustible.codigo_combustible] = reg.litros_producidos
            else:
                plantas[reg.codigo_combustible.zona_produccion.codigo_planta][reg.codigo_combustible.codigo_combustible] += reg.litros_producidos
        print(plantas)
        return Response(plantas)

@api_view(['GET'])
def gasolina_por_mes_ano(request,mes=datetime.datetime.now().month,ano=datetime.datetime.now().year):
    if request.method == 'GET':
        plantas = {}
        lista_registro = RegistroProduccion.objects.filter(fecha_produccion__year=ano, fecha_produccion__month=mes).all()
        for reg in lista_registro:
            if reg.codigo_combustible.zona_produccion.codigo_planta not in plantas:
                plantas[reg.codigo_combustible.zona_produccion.codigo_planta] = {}
            if reg.codigo_combustible.codigo_combustible not in plantas[reg.codigo_combustible.zona_produccion.codigo_planta]:
                plantas[reg.codigo_combustible.zona_produccion.codigo_planta][reg.codigo_combustible.codigo_combustible] = reg.litros_producidos
            else:
                plantas[reg.codigo_combustible.zona_produccion.codigo_planta][reg.codigo_combustible.codigo_combustible] += reg.litros_producidos
        print(plantas)
        return Response(plantas)

@api_view(['GET'])
def gasolina_por_ano(request,ano=datetime.datetime.now().year):
    if request.method == 'GET':
        plantas = {}
        lista_registro = RegistroProduccion.objects.filter(fecha_produccion__year=ano).all()
        for reg in lista_registro:
            if reg.codigo_combustible.zona_produccion.codigo_planta not in plantas:
                plantas[reg.codigo_combustible.zona_produccion.codigo_planta] = {}
            if reg.codigo_combustible.codigo_combustible not in plantas[reg.codigo_combustible.zona_produccion.codigo_planta]:
                plantas[reg.codigo_combustible.zona_produccion.codigo_planta][reg.codigo_combustible.codigo_combustible] = reg.litros_producidos
            else:
                plantas[reg.codigo_combustible.zona_produccion.codigo_planta][reg.codigo_combustible.codigo_combustible] += reg.litros_producidos
        print(plantas)
        return Response(plantas)

@api_view(['GET'])
def gasolina_por_mes(request,mes=datetime.datetime.now().month):
    if request.method == 'GET':
        plantas = {}
        lista_registro = RegistroProduccion.objects.filter(fecha_produccion__month=mes).all()
        for reg in lista_registro:
            if reg.codigo_combustible.zona_produccion.codigo_planta not in plantas:
                plantas[reg.codigo_combustible.zona_produccion.codigo_planta] = {}
            if reg.codigo_combustible.codigo_combustible not in plantas[reg.codigo_combustible.zona_produccion.codigo_planta]:
                plantas[reg.codigo_combustible.zona_produccion.codigo_planta][reg.codigo_combustible.codigo_combustible] = reg.litros_producidos
            else:
                plantas[reg.codigo_combustible.zona_produccion.codigo_planta][reg.codigo_combustible.codigo_combustible] += reg.litros_producidos
        print(plantas)
        return Response(plantas)