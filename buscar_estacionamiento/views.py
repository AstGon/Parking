from django.shortcuts import redirect, render
from .models import Estacionamiento, Arrendamiento
from datetime import datetime
from django.db.models import Q
import pytz
from decimal import Decimal

def login(request):
    return render(request, 'buscar_estacionamiento/login.html')

def registro_usuario(request):
    return render(request, 'buscar_estacionamiento/registro_usuario.html')


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
        fecha_fin = tz.localize(datetime.strptime(fecha_fin, '%Y-%m-%d'))
        hora_fin = tz.localize(datetime.strptime(hora_fin, '%H:%M'))

        fecha_inicio_formulario = datetime.combine(fecha_inicio.date(), hora_inicio.time()).astimezone(tz)

        # Obtén la fecha y hora actual con la misma zona horaria
        ahora = datetime.now(tz)

        # Inicializa la variable estacionamientos_disponibles
        estacionamientos_disponibles = []

        tiempo_transcurrido = fecha_fin - fecha_inicio + (hora_fin - hora_inicio)
        # Calcula las horas totales
        horas_totales = tiempo_transcurrido.total_seconds() / 3600

        # Comprueba las condiciones de fecha y hora
        if ahora <= fecha_inicio_formulario:
            # Filtra estacionamientos disponibles
            estacionamientos_disponibles = Estacionamiento.objects.exclude(
                id__in=Arrendamiento.objects.filter(
                    Q(fecha_fin__gte=fecha_inicio, fecha_inicio__lte=fecha_fin) &
                    Q(hora_fin__gte=hora_inicio, hora_inicio__lte=hora_fin)
                ).values('estacionamiento__id')
            ).filter(comuna__comuna=comuna)
            
        print(horas_totales)

        # Pasa los valores calculados al contexto
        return render(request, 'buscar_estacionamiento/mostrar_estacionamiento.html', {
            'estacionamientos_disponibles': estacionamientos_disponibles,
            'horas_totales': horas_totales,
        })

    return render(request, 'buscar_estacionamiento/buscar_estacionamiento.html')

def mostrar_estacionamiento(request, estacionamiento_id):
    if request.method == 'GET':
        # Busca el estacionamiento seleccionado en la base de datos
        try:
            estacionamiento_seleccionado = Estacionamiento.objects.get(id=estacionamiento_id)
        except Estacionamiento.DoesNotExist:
            # Maneja el caso si el estacionamiento no se encuentra
            # Redirige al usuario a una página de error o a donde desees
            return redirect('pagina_de_error')  # Reemplaza 'pagina_de_error' con la URL deseada

        # Lógica para calcular el precio total
        costo_por_hora = estacionamiento_seleccionado.costo_por_hora
        horas_totales = ...  # Debes obtener esto de alguna manera
        precio_total = costo_por_hora * horas_totales
        print(precio_total)
        return render(request, 'buscar_estacionamiento/mostrar_estacionamiento.html', {
            'estacionamiento_seleccionado': estacionamiento_seleccionado,
            'horas_totales': horas_totales,
            'precio_total': precio_total,
        })
    else:
        return redirect('pagina_de_error')
