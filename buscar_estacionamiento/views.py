from pyexpat.errors import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .models import Estacionamiento, Arrendamiento,Dueno,Cliente,User
from datetime import datetime
from django.db.models import Q
import pytz
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import ClienteRegistrationForm 
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class registro_cliente(CreateView):
    template_name = 'registro_cliente.html'  # Crea un template HTML para el formulario de registro.
    form_class = ClienteRegistrationForm   # Usa el formulario de registro de usuario de Django.
    success_url = reverse_lazy('login')  # Redirige a la página de inicio de sesión después del registro.




def registro_dueno(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Crea una instancia de Dueño y asocia al usuario
            dueno = Dueno.objects.create(user=user)
            
            login(request, user)
            return redirect('dashboard_dueno')  # Redirige al panel de dueño
    else:
        form = UserCreationForm()
    return render(request, 'buscar_estacionamiento/registro_dueno.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, 'cliente') and user.cliente:
                return redirect('dashboard_cliente')
            elif hasattr(user, 'dueno') and user.dueno:
                return redirect('dashboard_dueno')

            # Manejar el caso en el que las credenciales no son válidas
            # Puedes mostrar un mensaje de error en la plantilla.
    return render(request, 'login.html')

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