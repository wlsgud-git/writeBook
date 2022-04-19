from weakref import ref
from django.http import JsonResponse
from itsdangerous import Serializer
from ..serializers import *
from ..models import Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.authentication import get_authorization_header
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import permission_classes, authentication_classes

@permission_classes([AllowAny])
class LoginApi(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data = request.data)
        res = Response()
        if serializer.is_valid():
            res.data = {
                'status': serializer.validated_data['status'],
                'message': serializer.validated_data['message'],
                'access_token': serializer.validated_data['access_token'],
                'refresh_token': serializer.validated_data['refresh_token'],
                'url': serializer.validated_data['url']
            }
            
        return res

@permission_classes([AllowAny])
class AccessTokenVeridate(APIView):
    def get(self, request, format = None):
        auth = get_authorization_header(request)
        token = auth.decode('utf-8')
        if token != "null":
            payload = decode_access_token(token)

            if payload:
                return Response({'status':200, 'message': "인증된 유저입니다"})
            else:
                refresh_token = request.COOKIES.get('refresh_token')[2:-1]
                refresh_token_verify = decode_refresh_token(refresh_token)
                if refresh_token_verify:
                    access_tokens = create_access_token(refresh_token_verify['email'], refresh_token_verify['admin'])
                    return Response({'status':200, 'message': '새 토큰을 발급합니다.', 'access_token': access_tokens})
        
        return Response({'status':500, 'message': "로그인이 필요합니다", 'url':"/common/login/"})

# class LogoutApi(APIView):
