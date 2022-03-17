from ..serializers import UserSerializer
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
    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(Users, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)