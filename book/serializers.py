from pyexpat import model
from attr import field
from rest_framework import serializers
from .models import Users
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'content', 'create_date']

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'author', 'content', 'create_date'] 