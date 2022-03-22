from rest_framework.response import Response
from attr import field
from rest_framework import serializers
from .models import Users
from rest_framework.validators import UniqueValidator
from django.core.validators  import validate_email
from django.core.exceptions  import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','username', 'nickname', 'email']

class ResisterSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #     required = True, 
    #     validators=[UniqueValidator(queryset=Users.objects.all())]
    # )

    class Meta:
        model = Users
        fields = ['username', 'nickname','email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }   
    def validate_email(self, value):
        try:
            validate_email(value)
            return True
        except ValidationError:
            return False
     
    def create(self, validated_data):
        user = Users.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            nickname = validated_data['nickname'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user