from rest_framework import serializers
from .models import Trip

class TripSerialization(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields='__all__'