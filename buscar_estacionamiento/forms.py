from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente, Dueno,Comuna


class ClienteRegistrationForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    rut = forms.CharField(max_length=12)
    telefono = forms.CharField(max_length=15)
    direccion = forms.CharField(max_length=100)
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all())
    email = forms.EmailField(max_length=254, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")

    class Meta:
        model = Cliente
        fields = ('email', 'password1', 'password2', 'nombre', 'apellido', 'rut', 'telefono', 'direccion', 'comuna')

class DuenoRegistrationForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    rut = forms.CharField(max_length=12)
    telefono = forms.CharField(max_length=15)
    direccion = forms.CharField(max_length=100)
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all())
    email = forms.EmailField(max_length=254, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")

    class Meta:
        model = Dueno
        fields = ('email', 'password1', 'password2', 'nombre', 'apellido', 'rut', 'telefono', 'direccion', 'comuna')
