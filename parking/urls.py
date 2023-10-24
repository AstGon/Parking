from django.urls import path

from buscar_estacionamiento import views


urlpatterns = [
    path('buscar_estacionamiento/', views.buscar_estacionamiento, name='buscar_estacionamiento'),
    path('login/', views.login, name='login'),
     path('registro/cliente/', views.registro_cliente, name='registro_cliente'),
    path('registro/dueno/', views.registro_dueno, name='registro_dueno'),

]
