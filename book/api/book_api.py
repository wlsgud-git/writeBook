from itsdangerous import Serializer
from rest_framework.views import APIView
from ..serializers import *
from ..models import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

# 슬라이드 이미지
@permission_classes([AllowAny])
class SliderImageList(APIView):
    def get(self, request, format = None):
        slide_image = Slider.objects.order_by('id')
        slider_image_serializer = SliderSerializer(slide_image, many = True)
        return Response(slider_image_serializer.data)

# 모든 책 리스트
@permission_classes([AllowAny])
class BooksList(APIView):
    def get(self, request, format = None):
        all_book = Books.objects.order_by('id')
        all_book_serializer = BooksSerializer(all_book, many=True)
        return Response(all_book_serializer.data)

# class BookMake(APIView):
#     def post(self, request, format = None):

# 완결난 책
@permission_classes([AllowAny])
class endBookList(APIView):
    def get(self, request, format = None):
        endBook = Books.objects.filter(making = False)
        endBook_serializer = BooksSerializer(endBook, many = True)
        return Response(endBook_serializer.data)

# 연재중인 가장 인기있는 순위 100개
@permission_classes([AllowAny])
class TopBookList(APIView):
    def get(self, request, formant = None):
        topbook = Books.objects.filter(making = True).order_by("like_count")[:100]
        topbook_serializer = BooksSerializer(topbook, many = True)
        return Response(topbook_serializer.data)

@permission_classes([AllowAny])
class AllBestBook(APIView):
    def get(self, request, format = None):
        all_best_book = Books.objects.order_by('like_count')[:20]
        all_best_book_serializer = BooksSerializer(all_best_book, many = True)
        return Response(all_best_book_serializer)