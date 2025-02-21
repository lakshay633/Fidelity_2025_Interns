from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Price
from .serializer import PriceSerialization
from rest_framework.viewsets import ViewSet
import requests

# Create your views here.
@api_view(['GET'])
def get_loc(request):
    try:
        prices = Price.objects.all()
        serialized_prices = PriceSerialization(prices, many=True)
        loc = requests.get('http://127.0.0.1:8000/loc/loc')
        return Response(loc,status=200)
    except Exception as e:
        return Response('error',status=500)

class PriceViews(ViewSet):
    def list(self,request):
        prices = Price.objects.all()
        serialized_prices = PriceSerialization(prices, many=True)
        return Response(serialized_prices.data, status=status.HTTP_200_OK)
    def retrieve(self, request, pk = None):
        if pk is not None:
            price = Price.objects.get(itemID=pk)
            serialized_price = PriceSerialization(price)
            return Response(serialized_price.data, status=status.HTTP_200_OK) 
        return Response({"error": "Price not found"}, status=status.HTTP_404_NOT_FOUND)       
    def create(self, request):
        serialized_price = PriceSerialization(data=request.data)
        if serialized_price.is_valid():
            serialized_price.save()
            return Response({"message": "Price created"}, status=status.HTTP_201_CREATED)
        return Response(serialized_price.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        if pk is not None:
            price = Price.objects.get(itemID=pk)
            price.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    def update(self, request, pk=None):
        if pk is not None:
            price = Price.objects.get(itemID=pk)
            serialized_price = PriceSerialization(price,data=request.data)
            if serialized_price.is_valid():
                serialized_price.save()
                return Response(serialized_price.data, status=status.HTTP_200_OK) 
        return Response(status=status.HTTP_400_BAD_REQUEST)
    