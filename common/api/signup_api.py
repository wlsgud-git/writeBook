from itsdangerous import Serializer
from ..serializers import *
from ..models import Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import permission_classes, authentication_classes

@permission_classes([AllowAny])
class ResisterApi(APIView):
    def post(self, request, format = None):
        error = {'status':400}
        serializer = ResisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'pathname': "/common/login/" })
        error['message'] = "이미 존재하는 이메일이거나 이메일 형식에 맞지 않습니다" if "email" in serializer.errors else "비밀번호는 8자 이상 영소문자 숫자 특수문자를 1개 이상 포함시켜야 합니다"
        return Response(error)