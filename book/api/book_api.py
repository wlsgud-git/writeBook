from itsdangerous import Serializer
from rest_framework.views import APIView
from ..serializers import *
from ..models import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# 모든 책 리스트
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

# 요일에 맞는 책
class DayOfBook(APIView):
    def get(self, request, format=None):
        param = request.GET.get('day')
        book_list = Books.objects.filter(create_day_of_week=param)
        book_serializer = BookSerializer(book_list, many = True)
        return Response(book_serializer.data)

# 완결난 책
class EndBookList(APIView):
    def get(self, request, format = None):
        books = Books.objects.filter(making = False)
        books_serializer = BookSerializer(books, many=True)
        return Response(books_serializer.data)

# 인기 많은 책 100개
# class TopBookList(APIView):

# 한개의 책 정보
class BookDetail(APIView):
    def get(self, request, format = None):
        param = request.GET.get('id')
        book = Books.objects.get(id = param)
        serializer = BookSerializer(book) 
        return Response({"status": 200, "data": serializer.data})

