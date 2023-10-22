from django.urls import path

from buscar_estacionamiento import views


urlpatterns = [
    path('buscar_estacionamiento/', views.buscar_estacionamiento, name='buscar_estacionamiento'),
    path('mostrar_estacionamiento/', views.mostrar_estacionamiento, name='mostrar_estacionamiento'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('agregar_vehiculo/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('guardar_vehiculo/', views.guardar_vehiculo, name='guardar_vehiculo')
]
