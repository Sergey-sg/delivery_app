from rest_framework import generics
from api.cart.serializers import CartItemSerializer, CustomerSerializer, OrderSerializer

from apps.cart.models import Cart, CartItem, Customer, Order
from shared.mixins.views_mixins import get_cart_id


class CartItemListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        cart_items = []
        try:
            cart = Cart.objects.get(cart_id=get_cart_id(self.request))
            cart_items = CartItem.objects.filter(cart=cart, active=True)
        except (CartItem.DoesNotExist, Cart.DoesNotExist):
            pass    
        return cart_items
    

class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetailAPIView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer    
