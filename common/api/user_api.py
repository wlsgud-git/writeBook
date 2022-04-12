from itsdangerous import Serializer
from ..serializers import *
from ..models import Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

class UserList(APIView):
    def get(self, request, format=None):
        users = Users.objects.order_by('id')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes([AllowAny])
class UserDetail(APIView):
    def get_object(self, email):
        try:
            return Users.objects.get(email = email)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, email,format=None):
        user = self.get_object(email)
        serializer = UserSerializer(user)
        return Response({"user":serializer.data})
    
    def put(self, request, email, format=None):
        user = self.get_object(email)
        serializer = UserSerializer(user, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, email, format=None):
        user = self.get_object(email)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
