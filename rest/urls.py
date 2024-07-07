from django.urls import path, include
from rest_framework import serializers, routers
from . import views



urlpatterns = [
    path('porplanta/', views.RegistroDetalle.as_view(), name='porplanta'),
    path('porplanta/ano/<int:ano>/mes/<int:mes>/', views.gasolina_por_mes_ano, name='porplantaporanoymes'),
    path('porplanta/ano/<int:ano>/', views.gasolina_por_ano, name='porplantaporano'),
    path('porplanta/mes/<int:mes>/', views.gasolina_por_mes, name='porplantapormes'),
]