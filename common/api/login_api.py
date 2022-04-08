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

        if serializer.is_valid():
            jwt_token = serializer.validated_data['token']
            res = Response()
            res.set_cookie(key='jwt', value=jwt_token)
            res.data = {
                'jwt': jwt_token
            }
            return res
        
# class LogoutApi(APIView):
