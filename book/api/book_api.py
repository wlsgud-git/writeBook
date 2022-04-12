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
