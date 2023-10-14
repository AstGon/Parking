from django import forms

class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class BusquedaForm(forms.Form):
    communa = forms.CharField(max_length=100)
    fecha_inicio = forms.DateField()
    fecha_fin = forms.DateField()
    hora_inicio = forms.TimeField()
    hora_fin = forms.TimeField()