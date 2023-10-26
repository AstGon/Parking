from django.urls import path
from .import views

urlpatterns = [
    path('', views.buscar, name=''),
    path('buscar/', views.buscar, name='buscar'),
    path('cliente/register/', views.cliente_register, name='cliente_register'),
    path('dueno/register/', views.dueno_register, name='dueno_register'),
    path('autenticar/login_view', views.login_view, name='login'),

]