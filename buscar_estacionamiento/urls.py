from django.urls import path
from .import views

urlpatterns = [
    path('buscar/', views.buscar, name='buscar'),
    path('cliente/register/', views.cliente_register, name='cliente_register'),
    path('dueno/register/', views.dueno_register, name='dueno_register'),
    path('login_view', views.login_view, name='login')
]