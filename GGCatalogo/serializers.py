from .models import Juego
from rest_framework import serializers

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
          model = Juego
          fields ='__all__'