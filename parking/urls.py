from django.urls import path
from buscar_estacionamiento import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('buscar_estacionamiento/', views.buscar_estacionamiento, name='buscar_estacionamiento'),
    path('cliente/register/', views.cliente_register, name='cliente_register'),
    path('dueno/register/', views.dueno_register, name='dueno_register'),
    path('login/', views.login_view, name='login'),
    path("loginForm/", views.loginForm, name="loginForm"),
]

