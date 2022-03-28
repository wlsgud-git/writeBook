from itsdangerous import Serializer
from ..serializers import *
from ..models import Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class LoginApi(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data = request.data)

        if serializer.is_valid():
            return Response({'status':200})
        