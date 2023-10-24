from django.urls import path

from buscar_estacionamiento import views


urlpatterns = [
    path('buscar_estacionamiento/', views.buscar_estacionamiento, name='buscar_estacionamiento'),
    path('login/', views.login, name='login'),
    path('registro_dueno/', views.registro_dueno, name='registro_dueno'),
    path('registro_cliente/', views.registro_cliente, name='registro_cliente'),

]
