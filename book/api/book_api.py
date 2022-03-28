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
    
    def post(self, request, format = None):
        serializer = BookSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                "data": serializer.data
            })
        return Response({'status':400, 'data':"no response error"})

class BookDetail(APIView):
    def get(self, request, format = None):
        param = request.GET.get('id')
        book = Books.objects.get(id = param)
        serializer = BookSerializer(book) 
        return Response({"status": 200, "data": serializer.data})

