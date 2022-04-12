from rest_framework.response import Response
from attr import field
from rest_framework import serializers
from .models import Users
from rest_framework.validators import UniqueValidator
from django.core.validators  import validate_email
from django.core.exceptions  import ValidationError
from django.contrib import auth 
from rest_framework_jwt.settings import api_settings
import jwt, datetime
from writeBook.settings import SECRET_KEY, ALGORITHM
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

        user.set_password(validated_data['password'])
        user.save()
        return user

# 유저 로그인
class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)
    
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        user = auth.authenticate(email = email, password = password)
        
        if user is None:
            return False
        try:
            payload = {
                'user_email': email,
                'exp' : datetime.datetime.now() + datetime.timedelta(minutes=1),
                'iat' : datetime.datetime.now()
            }
            jwt_token = jwt.encode(payload, SECRET_KEY, ALGORITHM)
        except Users.DoesNotExist:
            raise serializers.ValidationError(
                'user is fuck that'
            )
        return {
            "token": jwt_token
        }