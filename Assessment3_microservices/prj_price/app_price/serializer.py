from rest_framework import serializers
from .models import Price

class PriceSerialization(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields='__all__'