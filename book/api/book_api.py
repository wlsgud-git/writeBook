from itsdangerous import Serializer
from rest_framework.views import APIView
from ..serializers import *
from ..models import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# 슬라이드 이미지
class SliderImageList(APIView):
    def get(self, request, format = None):
        slide_image = Slider.objects.order_by('id')
        slider_image_serializer = SliderSerializer(slide_image, many = True)
        return Response(slider_image_serializer.data)

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
        books = Books.objects.filter(making = False).order_by("-id")[:3]
        books_serializer = BookSerializer(books, many=True)
        return Response(books_serializer.data)

# 인기 많은 책 100개
class TopBookList(APIView):
    def get(self, request, format = None):
        topbook = Books.objects.filter(making=  True).order_by('like_book')[:100]
        topbook_serializer = BookSerializer(topbook, many= True)
        return Response(topbook_serializer.data)

# 한개의 책 정보
class BookDetail(APIView):
    def get(self, request, format = None):
        param = request.GET.get('id')
        book = Books.objects.get(id = param)
        serializer = BookSerializer(book) 
        return Response({"status": 200, "data": serializer.data})

# 역대 인기순 책
class AllTimeBestBook(APIView):
    def get(self, request, format = None):
        all_time_best_book = Books.objects.order_by('like_book')[:10]
        serializer = BookSerializer(all_time_best_book, many = True)
        return Response(serializer.data)
