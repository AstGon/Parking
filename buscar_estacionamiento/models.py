from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Comuna(models.Model):
    comuna = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=True)

class Vehiculo(models.Model):
    patente = models.CharField(max_length=7)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Dueno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=True)

class Estacionamiento(models.Model):
    direccion = models.CharField(max_length=200)
    dueño = models.ForeignKey(Dueno, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    costo_por_hora = models.IntegerField(default=0)


class Arrendamiento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio = models.IntegerField()
    hora_inicio = models.TimeField(default="00:00")
    hora_fin = models.TimeField(default="00:00")

class Reporte(models.Model):
    estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion = models.TextField()
    monto_recaudado = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)

