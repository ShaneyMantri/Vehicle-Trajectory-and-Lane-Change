from rest_framework import serializers
from .models import  image_received
from django.contrib.auth.models import User



class ImageReceivedSerializer(serializers.ModelSerializer):
    class Meta:
        model = image_received
        fields = "__all__"



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user



class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields = ('username','password')


