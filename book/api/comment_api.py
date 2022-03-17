from rest_framework.views import APIView
from ..serializers import *
from ..models import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class CommentsList(APIView):
    def get(self, request, format = None):
        comments = Comments.objects.order_by('id')
        serializers = CommentsSerializer(comments, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
class CommentDetail(APIView):
    def get_object(self, pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentsSerializer(comment, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
