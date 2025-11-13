from .models import Voucher, Cart, Cart_dish
from rest_framework import serializers

class VoucherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Voucher
        fields = '__all__'

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['user'] 

class CartDishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Cart_dish 
        fields = '__all__'
