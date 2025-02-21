from rest_framework.response import Response
from rest_framework import status
from .models import Trip
from .serializer import TripSerialization
from rest_framework.viewsets import ViewSet
# Create your views here.

class TripViews(ViewSet):
    def list(self,request):
        trips = Trip.objects.all()
        serialized_trips = TripSerialization(trips, many=True)
        return Response(serialized_trips.data, status=status.HTTP_200_OK)
    def retrieve(self, request, pk = None):
        if pk is not None:
            trip = Trip.objects.get(tripID=pk)
            serialized_trip = TripSerialization(trip)
            return Response(serialized_trip.data, status=status.HTTP_200_OK) 
        return Response({"error": "Trip not found"}, status=status.HTTP_404_NOT_FOUND)       
    def create(self, request):
        serialized_trip = TripSerialization(data=request.data)
        if serialized_trip.is_valid():
            serialized_trip.save()
            return Response({"message": "Trip created"}, status=status.HTTP_201_CREATED)
        return Response(serialized_trip.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        if pk is not None:
            trip = Trip.objects.get(tripID=pk)
            trip.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    def update(self, request, pk=None):
        if pk is not None:
            trip = Trip.objects.get(tripID=pk)
            serialized_trip = TripSerialization(trip,data=request.data)
            if serialized_trip.is_valid():
                serialized_trip.save()
                return Response(serialized_trip.data, status=status.HTTP_200_OK) 
        return Response(status=status.HTTP_400_BAD_REQUEST) 
    def duration(self, request):
        trips = Trip.objects.all().values('boarding', 'destination', 'tripDuration')
        return Response(trips, status=status.HTTP_200_OK)
    def getByDate(self, request, tripDate=None):
        if tripDate is not None:
            trips = Trip.objects.filter(tripDate=tripDate)
            serialized_trips = TripSerialization(trips, many=True)
            return Response(serialized_trips.data, status=status.HTTP_200_OK)
        return Response({"error": "Invalid date"}, status=status.HTTP_400_BAD_REQUEST)