from itsdangerous import Serializer
from ..serializers import *
from ..models import Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class ResisterApi(APIView):
    def post(self, request, format = None):
        serializer = ResisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200})
        return Response({'status': 400})