from django.db import models
from django.utils.crypto import get_random_string

class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=True)
    password = models.CharField(max_length=8, default=get_random_string)
    fecha_nacimiento = models.DateField(null=True)  # Agrega este campo



    class Meta:
        abstract = True

class Vehiculo(models.Model):
    patente = models.CharField(max_length=7, unique=True)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)

class Estacionamiento(models.Model):
    direccion = models.CharField(max_length=200)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    costo_por_hora = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dueno = models.ForeignKey('Dueno', on_delete=models.CASCADE)

class Cliente(Usuario):
    vehiculos = models.ManyToManyField(Vehiculo, blank=True, related_name='clientes_vehiculos')

class Dueno(Usuario):
    estacionamientos = models.ManyToManyField(Estacionamiento, blank=True, related_name='duenos_estacionamientos')

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
