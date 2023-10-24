from django.urls import path
from buscar_estacionamiento import views



urlpatterns = [
    path('buscar_estacionamiento/', views.buscar_estacionamiento, name='buscar_estacionamiento'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('cliente/register/', views.cliente_register, name='cliente_register'),
    path('dueno/register/', views.dueno_register, name='dueno_register'),
]

