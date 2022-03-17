from rest_framework.views import APIView
from ..serializers import *
from ..models import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class BookList(APIView):
    def get(self, request, format = None):
        books = Books.objects.order_by('id')
        serializers = BookSerializer(books, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
class BookDetail(APIView):
    def get_object(self, pk):
        try:
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(Books, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
