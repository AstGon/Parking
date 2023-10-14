from asyncio import AbstractServer
from django.conf import settings
from django.db import models

class CustomUser(AbstractServer):
    cliente = models.BooleanField(default=False)
    dueno = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)



class Comuna(models.Model):
    comuna = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    comuna_id = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    email = models.CharField(max_length=254,null=True)

class Vehiculo(models.Model):
    patente = models.CharField(max_length=7)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Dueno(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    comuna_id = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    email = models.CharField(max_length=254,null=True)

class Estacionamiento(models.Model):
    ubicacion = models.CharField(max_length=200)
    capacidad = models.IntegerField()
    dueño_id = models.ForeignKey(Dueno, on_delete=models.CASCADE)


class Arrendamiento(models.Model):
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estacionamiento_id = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio = models.IntegerField()
    hora_inicio = models.TimeField(default="00:00:00")
    hora_fin = models.TimeField(default="00:00:00")


class Reporte(models.Model):
    estacionamiento_id = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion = models.TextField()
    monto_recaudado = models.DecimalField(max_digits=10, decimal_places=2)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vehiculo_id = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)