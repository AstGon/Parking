from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class Comuna(models.Model):
    comuna = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)


# Define un administrador de usuario personalizado
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user=self._create_user(email, password, True, True, **extra_fields)
        return user

# Define un modelo de usuario personalizado
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

# Define modelos para grupos y permisos
class CustomGroup(Group):
    # Agrega campos adicionales si es necesario
    pass

class CustomPermission(Permission):
    # Agrega campos adicionales si es necesario
    pass

# Asigna modelos de grupo y permiso personalizados
class Cliente(CustomUser):
    # Agrega campos específicos del cliente aquí
    pass

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Dueno(CustomUser):
    # Agrega campos específicos del dueño aquí
    pass

    class Meta:
        verbose_name = 'Dueño'
        verbose_name_plural = 'Dueños'


class Vehiculo(models.Model):
    patente = models.CharField(max_length=7)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Estacionamiento(models.Model):
    direccion = models.CharField(max_length=200)
    dueno = models.ForeignKey(Dueno, on_delete=models.CASCADE)
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

