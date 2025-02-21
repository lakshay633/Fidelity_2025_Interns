from rest_framework.response import Response
from rest_framework import status
from .models import Loc
from .serializer import LocSerialization
from rest_framework.viewsets import ViewSet
# Create your views here.

class LocViews(ViewSet):
    def list(self,request):
        locs = Loc.objects.all()
        serialized_locs = LocSerialization(locs, many=True)
        return Response(serialized_locs.data, status=status.HTTP_200_OK)
    def retrieve(self, request, pk = None):
        if pk is not None:
            loc = Loc.objects.get(pincode=pk)
            serialized_loc = LocSerialization(loc)
            return Response(serialized_loc.data, status=status.HTTP_200_OK) 
        return Response({"error": "Loc not found"}, status=status.HTTP_404_NOT_FOUND)       
    def create(self, request):
        serialized_loc = LocSerialization(data=request.data)
        if serialized_loc.is_valid():
            serialized_loc.save()
            return Response({"message": "Loc created"}, status=status.HTTP_201_CREATED)
        return Response(serialized_loc.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        if pk is not None:
            loc = Loc.objects.get(pincode=pk)
            loc.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    def update(self, request, pk=None):
        if pk is not None:
            loc = Loc.objects.get(pincode=pk)
            serialized_loc = LocSerialization(loc,data=request.data)
            if serialized_loc.is_valid():
                serialized_loc.save()
                return Response(serialized_loc.data, status=status.HTTP_200_OK) 
        return Response(status=status.HTTP_400_BAD_REQUEST) 