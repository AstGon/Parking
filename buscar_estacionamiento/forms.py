from imaplib import _Authenticator
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente,Dueno, Comuna
from django.contrib.auth.forms import AuthenticationForm

class DuenoRegistrationForm(UserCreationForm):
    # Agregar campos específicos de Dueno aquí
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    rut = forms.CharField(max_length=12)
    telefono = forms.CharField(max_length=15)
    direccion = forms.CharField(max_length=100)
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all())

    class Meta:
        model = Dueno
        fields = ('email', 'password1', 'password2', 'nombre', 'apellido', 'rut', 'telefono', 'direccion', 'comuna')

class ClienteRegistrationForm(UserCreationForm):
    # Agregar campos específicos de Cliente aquí
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    rut = forms.CharField(max_length=12)
    telefono = forms.CharField(max_length=15)
    direccion = forms.CharField(max_length=100)
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all())

    class Meta:
        model = Cliente
        fields = ('email', 'password1', 'password2', 'nombre', 'apellido', 'rut', 'telefono', 'direccion', 'comuna')        

class LoginForm(AuthenticationForm):
    # Define los campos email y password para el formulario
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)