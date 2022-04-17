from rest_framework.response import Response
from attr import field
from rest_framework import serializers
from .models import Users
from rest_framework.validators import UniqueValidator
from django.core.validators  import validate_email
from django.core.exceptions  import ValidationError
from django.contrib import auth 
import bcrypt
from .token import *
from helper import pwValidate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'nickname', 'email']

# 유저 등록
class ResisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length= 200, validators=[UniqueValidator(queryset=Users.objects.all())])
    password = serializers.CharField(max_length = 30, write_only= True)

    class Meta:
        model = Users
        fields = ['username', 'nickname','email', 'password']

    def validate(self, attrs):
        if pwValidate(attrs['password'].lower()) == False:
            raise serializers.ValidationError('password so short')

        return attrs
    
    def create(self, validated_data):
        user = Users.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            nickname = validated_data['nickname'],
        )
        password = validated_data['password']

        user.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user.save()
        return user

# 유저 로그인
class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)
    
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        try:
            user = Users.objects.get(email = email)
            db_user_pw = user.password
        except Users.DoesNotExist:
            raise serializers.ValidationError("no exist user")

        if bcrypt.checkpw(password.encode('utf-8'), db_user_pw.encode("utf-8")):

            access_token = create_access_token(user.email, user.is_staff)
            refresh_token = create_refresh_token(user.email, user.is_staff)

            return {'access_token': access_token, 'refresh_token': refresh_token}
            
        raise serializers.ValidationError('no exist user')
     