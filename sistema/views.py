from imaplib import _Authenticator
from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import CustomAuthenticationForm

def index(request):
    context = {"user": request.user}

    return render(request, "sistema/index.html", context)

def loginForm(request):
    # Tu lógica para la vista de inicio de sesión aquí
    return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Autenticar al usuario
            user = AuthenticationError(request, username=username, password=password)

            if user is not None:
                # Si las credenciales son válidas, autenticar al usuario y redirigirlo
                login(request, user)
                if user.customuser.cliente:
                    return redirect('cliente_dashboard')
                elif user.customuser.dueno:
                    return redirect('dueno_dashboard')
                elif user.customuser.admin:
                    return redirect('admin_dashboard')
            else:
                # Tratar el caso de credenciales inválidas
                # Puedes agregar un mensaje de error al formulario o realizar alguna otra acción
                form.add_error(None, "Credenciales inválidas. Por favor, inténtelo de nuevo.")
        else:
            # Tratar el caso en el que el formulario no es válido (por ejemplo, campos faltantes)
            # Puedes agregar un manejo específico para esto si es necesario
            pass
    else:
        # Si la solicitud es un GET, mostrar el formulario vacío
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})