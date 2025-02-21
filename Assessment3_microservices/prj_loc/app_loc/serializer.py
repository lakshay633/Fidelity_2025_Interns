from rest_framework import serializers
from .models import Loc

class LocSerialization(serializers.ModelSerializer):
    class Meta:
        model = Loc
        fields='__all__'