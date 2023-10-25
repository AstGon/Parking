
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("buscar_estacionamiento/", include("buscar_estacionamiento.urls")),
    path("buscar_estacionamiento/",include('django.contrib.auth.urls')),
]
