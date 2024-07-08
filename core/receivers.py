from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_delete
from django.dispatch import receiver
from django.db.models import Sum
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv
from .models import RegistroAcciones, RegistroProduccion

load_dotenv()
client = WebClient(token=os.getenv('SLACK_BOT_TOKEN'))

@receiver(post_save, sender=RegistroProduccion)
def actualizar_registro(sender, instance, created,**kwargs):
    totales = RegistroProduccion.objects.filter(codigo_combustible=instance.codigo_combustible).aggregate(suma=Sum('litros_producidos'))
    print(totales['suma'])
    #obtener usuario
    import inspect
    request = None
    for fr in inspect.stack():
        if fr[3] == 'get_response':
            request = fr[0].f_locals['request']
            break
    usuario = request.user
    if created:
        RegistroAcciones.objects.create(usuario=usuario.username,accion="CRE",registro=instance.id)
        # mensaje Slack
        response = client.chat_postMessage(channel='#producttracker', text=f"{ instance.fecha_produccion } { instance.hora_registro } { instance.codigo_combustible.zona_produccion.codigo_planta } - Nuevo Registro de Produccion - { instance.codigo_combustible.codigo_combustible } {instance.litros_producidos} litros | Total Almacenado { totales['suma'] }")
    else:
        RegistroAcciones.objects.create(usuario=usuario.username,accion="MOD",registro=instance.id)
        # mensaje Slack
        response = client.chat_postMessage(channel='#producttracker', text=f"{ instance.fecha_produccion } { instance.hora_registro } { instance.codigo_combustible.zona_produccion.codigo_planta } - Modificacion de registro de Produccion - { instance.codigo_combustible.codigo_combustible } {instance.litros_producidos} litros | Total Almacenado { totales['suma'] }")


@receiver(pre_delete, sender=RegistroProduccion)
def guardar_eliminacion(sender, instance,**kwargs):
    #obtener usuario
    import inspect
    request = None
    for fr in inspect.stack():
        if fr[3] == 'get_response':
            request = fr[0].f_locals['request']
            break
    usuario = request.user

    totales = RegistroProduccion.objects.filter(codigo_combustible=instance.codigo_combustible).aggregate(Sum('litros_producidos'))
    RegistroAcciones.objects.create(usuario=usuario.username,accion="ELI",registro=instance.id)
    response = client.chat_postMessage(channel='#producttracker', text=f"{ instance.fecha_produccion } { instance.hora_registro } { instance.codigo_combustible.zona_produccion.codigo_planta } - Eliminacion de Registro de Produccion - { instance.codigo_combustible.codigo_combustible } {instance.litros_producidos} litros")