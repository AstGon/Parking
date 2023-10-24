from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente, Dueno,Comuna
from django.contrib.auth.models import User

class ClienteRegistrationForm(forms.ModelForm):
    username = forms.EmailField(max_length=254, required=True)
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    rut = forms.CharField(max_length=12)
    telefono = forms.CharField(max_length=15)
    direccion = forms.CharField(max_length=100)
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all())
    password1 = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'nombre', 'apellido', 'rut', 'telefono', 'direccion', 'comuna')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class DuenoRegistrationForm(forms.ModelForm):
    username = forms.EmailField(max_length=254, required=True)    
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    rut = forms.CharField(max_length=12)
    telefono = forms.CharField(max_length=15)
    direccion = forms.CharField(max_length=100)
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all())
    password1 = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'nombre', 'apellido', 'rut', 'telefono', 'direccion', 'comuna')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user