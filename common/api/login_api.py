from django.http import JsonResponse
from itsdangerous import Serializer
from ..serializers import *
from ..models import Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import permission_classes, authentication_classes

@permission_classes([AllowAny])
class LoginApi(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data = request.data)
        error = {"status": 400}
        if serializer.is_valid():
            access_token = serializer.validated_data['access_token']
            refresh_token = serializer.validated_data['refresh_token']

            res = Response()
            res.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
            res.data = {'status': 200, 'message':"로그인이 완료되었습니다", 'access_token':access_token, "url": '/book'}
            return res
        error['message'] = '로그인 정보가 시스템에 있는 정보와 맞지 않습니다'
        return Response(error)

# class LogoutApi(APIView):
