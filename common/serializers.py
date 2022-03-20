from attr import field
from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','username', 'nickname', 'email']

class ResisterSerializer(serializers.ModelSerializer):
     
    password = serializers.CharField(write_only = True)

    class Meta:
        model = Users
        fields= ['username', 'nickname', 'email', 'password']
    
    

    