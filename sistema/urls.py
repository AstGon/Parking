from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login_view, name='login'), 
    path('resultado_busqueda/', views.resultado_busqueda, name='resultado_busqueda'),
]
