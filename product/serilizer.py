from .models import Product
from django.contrib.auth.models import User

from rest_framework import serializers


class ProductSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'
        

class UserSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'