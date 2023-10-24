from pyexpat.errors import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Estacionamiento, Arrendamiento,Dueno,Cliente
from datetime import datetime
from django.db.models import Q
import pytz
from django.shortcuts import render, redirect
from .forms import ClienteRegistrationForm, CustomAuthenticationForm, DuenoRegistrationForm,ClienteRegistrationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model

User = get_user_model()



def cliente_register(request):
    if request.method == 'POST':
        form = ClienteRegistrationForm(request.POST)
        if form.is_valid():
            # Crear una instancia de Cliente
            user = form.save(commit=False)  # Guarda el formulario sin guardar en la base de datos
            user.save()
            cliente = Cliente.objects.create(user=user)  # Crea una instancia de Cliente relacionada
            # Asigna otros campos específicos de Cliente
            cliente.nombre = form.cleaned_data['nombre']
            # Completa otros campos específicos de Cliente

            login(request, user)
            return redirect('ruta_de_redireccion_cliente')
    else:
        form = ClienteRegistrationForm()
    return render(request, 'buscar_estacionamiento/registro_cliente.html', {'form': form})

def dueno_register(request):
    if request.method == 'POST':
        form = DuenoRegistrationForm(request.POST)
        if form.is_valid():
            # Crear una instancia de Dueno
            user = form.save(commit=False)  # Guarda el formulario sin guardar en la base de datos
            user.save()
            dueno = Dueno.objects.create(user=user)  # Crea una instancia de Dueno relacionada
            # Asigna otros campos específicos de Dueno
            dueno.nombre = form.cleaned_data['nombre']
            # Completa otros campos específicos de Dueno

            login(request, user)
            return redirect('ruta_de_redireccion_dueno')
    else:
        form = DuenoRegistrationForm()
    return render(request, 'buscar_estacionamiento/registro_dueno.html', {'form': form})




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


class CustomLoginView(LoginView):
    template_name = 'buscar_estacionamiento/login.html'
    form_class = CustomAuthenticationForm  # Usa tu formulario personalizado
    success_url = reverse_lazy('buscar_estacionamiento')