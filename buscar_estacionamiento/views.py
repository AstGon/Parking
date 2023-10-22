from django.shortcuts import render
from .models import Estacionamiento, Arrendamiento
from datetime import datetime
from django.db.models import Q
import pytz

def buscar_estacionamiento(request):
    if request.method == 'POST':
        comuna = request.POST.get('comuna')
        fecha_inicio = request.POST.get('fecha_inicio')
        hora_inicio = request.POST.get('hora_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        hora_fin = request.POST.get('hora_fin')

        # Crea objetos de zona horaria para asegurarte de que se manejen correctamente las fechas y horas
        tz = pytz.timezone('America/Santiago')

        fecha_inicio = tz.localize(datetime.strptime(fecha_inicio, '%Y-%m-%d'))
        hora_inicio = tz.localize(datetime.strptime(hora_inicio, '%H:%M'))

        fecha_inicio_formulario = datetime.combine(fecha_inicio.date(), hora_inicio.time()).astimezone(tz)

        # Obtén la fecha y hora actual con la misma zona horaria
        ahora = datetime.now(tz)

        # Inicializa la variable estacionamientos_disponibles
        estacionamientos_disponibles = []

        # Comprueba las condiciones de fecha y hora
        if ahora <= fecha_inicio_formulario:
            # Filtra estacionamientos disponibles
            estacionamientos_disponibles = Estacionamiento.objects.exclude(
                id__in=Arrendamiento.objects.filter(
                    Q(fecha_fin__gte=fecha_inicio, fecha_inicio__lte=fecha_fin) &
                    Q(hora_fin__gte=hora_inicio, hora_inicio__lte=hora_fin)
                ).values('estacionamiento__id')
            ).filter(comuna__comuna=comuna)

        return render(request, 'buscar_estacionamiento/mostrar_estacionamiento.html', {
            'estacionamientos_disponibles': estacionamientos_disponibles,
        })

    return render(request, 'buscar_estacionamiento/buscar_estacionamiento.html')


def mostrar_estacionamiento(request):
    return render(request, 'buscar_estacionamiento/mostrar_estacionamiento.html')

def perfil_usuario(request):
    return render(request, 'buscar_estacionamiento/perfil.html')

def agregar_vehiculo(request):
    return render(request, 'buscar_estacionamiento/agregar_vehiculo.html')


from django.shortcuts import render, redirect
from .models import Vehiculo

def guardar_vehiculo(request):
    if request.method == 'POST':
        patente = request.POST['patente']
        modelo = request.POST['modelo']
        marca = request.POST['marca']
        
        vehiculo = Vehiculo(patente=patente, modelo=modelo, marca=marca)
        vehiculo.save()
        return redirect('perfil_usuario')

    # Resto de la lógica, si es necesario
    # debería funcionar cuando se almacene en la bd
    

    return render(request, 'buscar_estacionamiento/agregar_vehiculo.html')
