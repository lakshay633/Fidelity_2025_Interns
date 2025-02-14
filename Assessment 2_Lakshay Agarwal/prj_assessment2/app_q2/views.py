from rest_framework.response import Response
from rest_framework import status
from .models import QuestionPaper
from .serializer import QuestionSerialization
from rest_framework.viewsets import ViewSet
# Create your views here.

class QuestionViews(ViewSet):
    def list(self,request):
        subs = QuestionPaper.objects.all()
        serialized_subs = QuestionSerialization(subs, many=True)
        return Response(serialized_subs.data, status=status.HTTP_200_OK)
    def retrieve(self, request, pk = None):
        if pk is not None:
            sub = QuestionPaper.objects.get(subject=pk)
            serialized_sub = QuestionSerialization(sub)
            return Response(serialized_sub.data, status=status.HTTP_200_OK) 
        return Response({"error": "QuestionPaper not found"}, status=status.HTTP_404_NOT_FOUND)       
    def create(self, request):
        serialized_sub = QuestionSerialization(data=request.data)
        if serialized_sub.is_valid():
            serialized_sub.save()
            return Response({"message": "QuestionPaper created"}, status=status.HTTP_201_CREATED)
        return Response(serialized_sub.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        if pk is not None:
            sub = QuestionPaper.objects.get(subject=pk)
            sub.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    def update(self, request, pk=None):
        if pk is not None:
            sub = QuestionPaper.objects.get(subject=pk)
            serialized_sub = QuestionSerialization(sub,data=request.data)
            if serialized_sub.is_valid():
                serialized_sub.save()
                return Response(serialized_sub.data, status=status.HTTP_200_OK) 
        return Response(status=status.HTTP_400_BAD_REQUEST) 