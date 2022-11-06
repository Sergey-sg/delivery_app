from dataclasses import fields
from rest_framework import serializers
from apps.shop.models import Product, Shop


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ('pk', 'name', 'slug', 'image', 'img_alt', 'phone', 'email',)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'pk', 'shop', 'name', 'slug', 'description', 
            'price', 'image', 'img_alt', 'stock', 'available'
        )        
