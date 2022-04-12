from pyexpat import model
from attr import field
from rest_framework import serializers
from common.models import Users
from .models import * 

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"
    
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['title', 'author', 'thumbnail', "create_day_of_week", "create_at"]