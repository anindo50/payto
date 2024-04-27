# serializers.py
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loginmodel
        fields = ['username', 'password']