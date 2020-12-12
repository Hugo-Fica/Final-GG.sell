from django.contrib import admin
from .models import Desarrollador, Genero, Juego, Idiomas, Inventario

# Register your models here.
admin.site.register(Idiomas)
admin.site.register(Genero)

@admin.register(Desarrollador)
class DesarrolladorAdmin(admin.ModelAdmin):
    list_display = ('desarrollador', 'creacion')
    fields = [('desarrollador'), 'creacion']

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'desarrollador', 'clasificacion')

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_filter = ('estado',)
    fieldsets = (
        ('Juego', {
            'fields': ('juegos', 'lanzamiento', 'idioma', 'id')
        }),
        ('Disponibilidad', {
            'fields': ('estado',)
        })
    )

# Register your models here.
