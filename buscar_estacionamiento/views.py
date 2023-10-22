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
    if request.method == 'GET':
        estacionamientos_disponibles = request.session.get('estacionamientos_disponibles', [])
        horas_totales = []
        valor_a_pagar = []

        for estacionamiento in estacionamientos_disponibles:
            # Calcula las horas totales para cada estacionamiento
            fecha_inicio = estacionamiento.fecha_inicio
            hora_inicio = estacionamiento.hora_inicio
            fecha_fin = estacionamiento.fecha_fin
            hora_fin = estacionamiento.hora_fin
            horas = calcular_horas_totales(fecha_inicio, hora_inicio, fecha_fin, hora_fin)
            horas_totales.append((estacionamiento.id, horas))

            # Calcula el precio para cada estacionamiento (ajusta esta lógica según tus necesidades)
            precio = calcular_precio(horas)
            valor_a_pagar.append((estacionamiento.id, precio))

        return render(request, 'buscar_estacionamiento/mostrar_estacionamiento.html', {
            'estacionamientos_disponibles': estacionamientos_disponibles,
            'horas_totales': horas_totales,
            'valor_a_pagar': valor_a_pagar,
        })
    else:
        return render(request, 'buscar_estacionamiento/mostrar_estacionamiento.html')

# Función para calcular las horas totales
def calcular_horas_totales(fecha_inicio, hora_inicio, fecha_fin, hora_fin):
    diferencia = fecha_fin - fecha_inicio
    horas_totales = (diferencia.days * 24) + (diferencia.seconds // 3600)
    horas_totales += (hora_fin.hour - hora_inicio.hour)
    return horas_totales

# Función para calcular el precio (ajusta esta lógica según tus necesidades)
def calcular_precio(horas_totales):
    precio_por_hora = 10  # Precio por hora, ajusta según tus necesidades
    return horas_totales * precio_por_hora