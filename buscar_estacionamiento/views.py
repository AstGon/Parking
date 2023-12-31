from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Estacionamiento, Arrendamiento,Dueno,Cliente
from datetime import datetime
from django.db.models import Q
import pytz
from .forms import ClienteRegistrationForm,DuenoRegistrationForm,ClienteRegistrationForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

User = get_user_model()

@login_required

def login_view(request):
    if request.method == 'POST':
        print("Vista de inicio de sesión ejecutada")
        form = LoginForm(request, data=request.POST)
        print("Antes de la validación del formulario")
        if form.is_valid():
            print("Formulario válido")
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("Usuario autenticado")
                login(request, user)
                return redirect('buscar')
            else:
                print("Error de autenticación")
        else:
            print("Formulario no válido")
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


def cliente_register(request):
    if request.method == 'POST':
        form = ClienteRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('buscar_estacionamiento/buscar.html')  # Cambia 'pagina_de_inicio' por la URL a la que quieres redirigir al usuario después del registro
    else:
        form = ClienteRegistrationForm()
    return render(request, 'buscar_estacionamiento/registro_cliente.html', {'form': form})

def dueno_register(request):
    if request.method == 'POST':
        form = DuenoRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('buscar_estacionamiento/buscar')  # Cambia 'pagina_de_inicio' por la URL a la que quieres redirigir al usuario después del registro
    else:
        form = DuenoRegistrationForm()
    return render(request, 'buscar_estacionamiento/registro_dueno.html', {'form': form})




def buscar(request):
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
    return render(request, 'buscar_estacionamiento/buscar.html')