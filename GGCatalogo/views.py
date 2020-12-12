from django.contrib.admin import autodiscover
from django.db import models
from django.shortcuts import render
from .models import Juego, Inventario, Desarrollador
from django.views import generic
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    numero_juego = Juego.objects.all().count()
    numero_inventario = Inventario.objects.all().count()
    numero_inventario_disponible = Inventario.objects.filter(estado__exact='d').count()
    numero_desarrolladores = Desarrollador.objects.count() # El all() esta implicido por defecto.

    # Numero de visitas a esta view, como está contado en la variable sesión
    numero_visitas = request.session.get('numero_visitas',0)
    request.session['numero_visitas'] = numero_visitas + 1

    # Renderiza la plantilla HTML index.html con los en la variable contexto
    return render(request, 
                 'index.html', 
                 context={'numero_juegos': numero_juego,
                            'numero_inventario': numero_inventario,
                            'numero_inventario_disponible': numero_inventario_disponible, 
                            'numero_autores': numero_desarrolladores,
                            'numero_visitas': numero_visitas,})

class JuegoListView(generic.ListView):
    model = Juego
    paginate_by = 10   

class JuegoDetailView(generic.DetailView):
    model = Juego

class DesarrolladorListView(generic.ListView):
    model = Desarrollador

class DesarrolladorDetailView(generic.DetailView):
    model = Desarrollador

