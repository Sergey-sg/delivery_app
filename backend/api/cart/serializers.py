from rest_framework import serializers
from api.shop.serializers import ProductSerializer

from ...apps.cart.models import CartItem, Customer, Order


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ('pk', 'product', 'cart', 'order', 'quantity', 'sub_total',)


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('pk', 'name', 'email', 'phone', 'address', 'geolocation',)
        

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('pk', 'customer', 'sent', 'total_price',)
