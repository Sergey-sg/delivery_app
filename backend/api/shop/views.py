from rest_framework import generics
from rest_framework.permissions import AllowAny
from api.shop.serializers import ProductSerializer, ShopSerializer
from apps.shop.filters import ProductFilter

from apps.shop.models import Product, Shop


class ShopListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ProductListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def get_queryset(self):
        qs =  super(ProductListAPIView, self).get_queryset()    
        if 'filter_shop' in self.request.GET and self.request.GET['filter_shop']:
            qs = qs.filter(shop__slug=self.request.GET['filter_shop'])
        return qs    


class ProductDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
