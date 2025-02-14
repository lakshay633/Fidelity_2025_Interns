from rest_framework.response import Response
from rest_framework import status
from .models import Planet
from .serializer import PlanetSerialization
from rest_framework.viewsets import ViewSet
# Create your views here.

class PlanetViews(ViewSet):
    def list(self,request):
        planets = Planet.objects.all()
        serialized_planets = PlanetSerialization(planets, many=True)
        return Response(serialized_planets.data, status=status.HTTP_200_OK)
    def retrieve(self, request, pk = None):
        if pk is not None:
            planet = Planet.objects.get(pId=pk)
            serialized_planet = PlanetSerialization(planet)
            return Response(serialized_planet.data, status=status.HTTP_200_OK) 
        return Response({"error": "Planet not found"}, status=status.HTTP_404_NOT_FOUND)       
    def create(self, request):
        serialized_planet = PlanetSerialization(data=request.data)
        if serialized_planet.is_valid():
            serialized_planet.save()
            return Response({"message": "Planet created"}, status=status.HTTP_201_CREATED)
        return Response(serialized_planet.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        if pk is not None:
            planet = Planet.objects.get(pId=pk)
            planet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    def update(self, request, pk=None):
        if pk is not None:
            planet = Planet.objects.get(Planet, pId=pk)
            serialized_planet = PlanetSerialization(data=request.data)
            if serialized_planet.is_valid():
                serialized_planet.save()
                return Response(serialized_planet.data, status=status.HTTP_200_OK) 
        return Response(status=status.HTTP_400_BAD_REQUEST) 