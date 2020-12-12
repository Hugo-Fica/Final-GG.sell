import uuid
from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.


class Genero(models.Model):
    nombreJuego = models.CharField(
        max_length=200, help_text='Ingrese el nombre del genero del Juego (Ej. Acción - Aventura)')

    def __str__(self):
        return self.nombreJuego


class Desarrollador(models.Model):
    desarrollador = models.CharField(max_length=100)
    creacion= models.DateField(
        'Creación', null=True, blank=True)

    class Meta:
        ordering = ['desarrollador']

    def __str__(self):
        return f'{self.desarrollador}'

    def get_absolute_url(self):
        return reverse("desarrollador_detail", args=[str(self.id)])


class Juego(models.Model):
    titulo = models.CharField(max_length=200)
    desarrollador = models.ForeignKey(Desarrollador, on_delete=models.SET_NULL, null=True)
    sinopsis = models.TextField(
        max_length=1000, help_text='Ingresa una breve descripción del juego')
    clasificacion = models.TextField(
        max_length=100, help_text='Ingresa una clasificacion del juego')
    genero = models.ManyToManyField(
        Genero, help_text='Seleccione un genero para este juego')
    foto = models.ImageField(upload_to='imagenes')

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("juegos_detail", args=[str(self.id)])


class Idiomas(models.Model):
    nombre = models.CharField(
        max_length=50, help_text='Ingrese los idiomas del juego (Ej. Español-Ingles-Japones-Chino Mandarin)')

    def __str__(self):
        return self.nombre


class Inventario(models.Model):
    ESTADO_JUEGO = (
        ('a', 'agotado'),
        ('pv', 'Pre-venta'),
        ('d', 'Disponible'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='ID es único para cada juego en particular en toda la tienda')
    juegos = models.ForeignKey(Juego, on_delete=models.SET_NULL, null=True)
    idioma = models.ForeignKey(Idiomas, on_delete=models.SET_NULL, null=True)
    lanzamiento = models.CharField(max_length=20)
    estado = models.CharField(max_length=2, choices=ESTADO_JUEGO,
                               blank=True, default='m', help_text='Disponibilidad de Juego')

    class Meta:
        ordering: ['disponibilidad']

    def __str__(self):
        return f'{self.id} ({self.juegos.titulo})'
