from rest_framework import serializers
from .models import Planet

class PlanetSerialization(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields='__all__'