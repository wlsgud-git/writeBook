from itsdangerous import Serializer
from ..serializers import *
from ..models import Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class UserList(APIView):
    def get(self, request, format=None):
        users = Users.objects.order_by('id')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserDetail(APIView):
    def get_object(self, user):
        try:
            return Users.objects.get(email = user)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        param = request.GET.get('u')
        user = self.get_object(param)
        serializer = UserSerializer(user)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def put(self, request, format=None):
        param = request.GET.get('u')
        user = self.get_object(param)
        serializer = UserSerializer(user, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        param = request.GET.get('u')
        user = self.get_object(param)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
