from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from .models import Product
from .serializer import ProductSerialization
from rest_framework.viewsets import ViewSet
# Create your views here.

class ProductViews(ViewSet):
    def list(self,request):
        products = Product.objects.all()
        serialized_products = ProductSerialization(products, many=True)
        return Response(serialized_products.data, status=status.HTTP_200_OK)
    def retrieve(self, request, pk = None):
        if pk is not None:
            product = Product.objects.get(productID=pk)
            serialized_product = ProductSerialization(product)
            return Response(serialized_product.data, status=status.HTTP_200_OK) 
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)       
    def create(self, request):
        serialized_product = ProductSerialization(data=request.data)
        if serialized_product.is_valid():
            serialized_product.save()
            return Response({"message": "Product created"}, status=status.HTTP_201_CREATED)
        return Response(serialized_product.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        if pk is not None:
            product = Product.objects.get(productID=pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    def update(self, request, pk=None):
        if pk is not None:
            product = Product.objects.get(productID=pk)
            serialized_product = ProductSerialization(product,data=request.data)
            if serialized_product.is_valid():
                serialized_product.save()
                return Response(serialized_product.data, status=status.HTTP_200_OK) 
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})