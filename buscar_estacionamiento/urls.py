from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.buscar, name=''),
    path('buscar/', views.buscar, name='buscar'),
    path('cliente/register/', views.cliente_register, name='cliente_register'),
    path('dueno/register/', views.dueno_register, name='dueno_register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

]