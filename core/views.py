from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Combustibles, Plantas, RegistroProduccion
# Create your views here.

def logging(request):
    if request.user.is_authenticated:
        return redirect(homePage)
    if (request.POST):
        usuario = request.POST['usuario']
        password = request.POST['contraseña']
        user = authenticate(request, username=usuario, password=password)

        if user is not None:
            login(request, user)
            return redirect(homePage)
    
    return render(request, 'core/login.html')

def loggingOut(request):
    logout(request)
    return redirect(logging)


def homePage(request):
    if not request.user.is_authenticated:
        return redirect(logging)

    filtrar = "1"
    if request.GET:
        filtrar = request.GET['filtrar']
    if filtrar == "1":
        registros = RegistroProduccion.objects.all()
    else:
        registros = RegistroProduccion.objects.filter(operador=request.user.username).all()

    combustibles = Combustibles.objects.all()

    data = {
        "tipo_combustibles" : combustibles,
        "registros" : registros
    }

    return render(request, 'core/homePage.html', data)

def nuevo(request):
    if (request.POST):
        operador = request.user.username
        combustible = request.POST['combustible']
        litros = request.POST['litros']
        fecha = request.POST['Fecha']
        hora = request.POST['hora']
        turno = request.POST['turno']
    
    registro = RegistroProduccion()
    registro.operador = operador
    registro.codigo_combustible = Combustibles.objects.filter(codigo_combustible=combustible).get()
    registro.litros_producidos = litros
    registro.fecha_produccion = fecha
    registro.turno = turno
    registro.hora_registro = hora

    registro.save()

    return redirect(homePage)

def editar_propuesta(request):
    if (request.GET):
        # Capturo datos del formulario
        id_registro = request.GET['id']
        combustible = request.GET['combustible']
        litros = request.GET['litros']
        fecha = request.GET['Fecha']
        hora = request.GET['hora']
        turno = request.GET['turno']

    # Construir y cargar el objeto con los datos del form
    registro = RegistroProduccion.objects.filter(id=id_registro).get()
    registro.codigo_combustible = Combustibles.objects.filter(codigo_combustible=combustible).get()
    registro.litros_producidos = litros
    registro.fecha_produccion = fecha
    registro.turno = turno
    registro.hora_registro = hora
    # Guardar en la base de datos
    registro.save()

    return redirect(homePage)