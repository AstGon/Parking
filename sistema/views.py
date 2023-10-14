
from django.shortcuts import render
from sistema.forms import BusquedaForm
from sistema.models import Estacionamiento


#Este codigo me lleva al index
def index(request):
    form = BusquedaForm()
    return render(request, "sistema/index.html", {'form': form})

#Esta es la funcion para buscar los estacionamientos
def busqueda(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            communa = form.cleaned_data['communa']
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            hora_inicio = form.cleaned_data['hora_inicio']
            hora_fin = form.cleaned_data['hora_fin']

            # Realiza la búsqueda en la base de datos
            results = Estacionamiento.objects.filter(
                communa=communa, rango_fecha =(fecha_inicio, fecha_fin), rango_tiempo=(hora_inicio,hora_fin)
            )

            return render(request, 'resultado_busqueda.html', {'results': results})
    return render(request, 'index.html')


def login_view(request):

    return render(request, 'sistema/login.html')

def resultado_busqueda(request):

    return render(request, 'sistema/resultado_busqueda.html')
