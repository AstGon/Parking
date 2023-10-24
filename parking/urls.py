from django.urls import path

from buscar_estacionamiento import views


urlpatterns = [
    path('buscar_estacionamiento/', views.buscar_estacionamiento, name='buscar_estacionamiento'),
    path('login/', views.login, name='login'),
    path('registro_usuario/', views.registro_usuario, name='registro_usuario'),
    path('tipousuario/', views.tipousuario, name='tipousuario'),

]


