from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .models import Estacionamiento, Arrendamiento
from datetime import datetime
from django.db.models import Q
import pytz
from decimal import Decimal


def login(request):
    error_message = None  # Inicializa la variable error_message
    if request.method == 'POST':
        email = request.POST['email']
        contraseña = request.POST['password']
        user = authenticate(request, email=email, password=contraseña)

        if user is not None:
            login(request, user)
            # El inicio de sesión fue exitoso
            return redirect('pagina_de_inicio')  # Redirige a la página de inicio
        else:
            # El inicio de sesión ha fallado, puedes mostrar un mensaje de error
            error_message = "El inicio de sesión ha fallado. Verifica tus credenciales."

    return render(request, 'buscar_estacionamiento/login.html', {'error_message': error_message})


def registro_usuario(request):
    return render(request, 'buscar_estacionamiento/registro_usuario.html')



def tipousuario(request):
    return render(request, 'buscar_estacionamiento/tipousuario.html')


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

        costo_por_hora = 0
        

        # Filtra estacionamientos disponibles
        if ahora <= fecha_inicio_formulario:
            estacionamientos_disponibles = Estacionamiento.objects.exclude(
                id__in=Arrendamiento.objects.filter(
                    Q(fecha_fin__gte=fecha_inicio, fecha_inicio__lte=fecha_fin) &
                    Q(hora_fin__gte=hora_inicio, hora_inicio__lte=hora_fin)
                ).values('estacionamiento__id')
            ).filter(comuna__comuna=comuna)
            

            for estacionamiento in estacionamientos_disponibles:
                costo_por_hora=estacionamiento.costo_por_hora
                print(horas_totales)
                print(costo_por_hora)
                estacionamiento.precio_total = costo_por_hora * horas_totales  # Calcula el precio total para este estacionamiento

        # Pasa los valores calculados al contexto
        return render(request, 'buscar_estacionamiento/mostrar_estacionamiento.html', {
            'estacionamientos_disponibles': estacionamientos_disponibles,
            'horas_totales': horas_totales,
            'costo_por_hora': costo_por_hora,
        })
    return render(request, 'buscar_estacionamiento/buscar_estacionamiento.html')