from .models import Voucher, Cart, Cart_dish
from rest_framework import serializers

class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user','id'] 

class CartDishSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cart_dish 
        fields = '__all__'
