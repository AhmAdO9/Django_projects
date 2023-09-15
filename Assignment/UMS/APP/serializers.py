from APP.models import *
from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth.models import User

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TO_DO
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'