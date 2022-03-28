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
class ResisterApi(APIView):
    def post(self, request, format = None):
        serializer = ResisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200})
        return Response({'status': 400})