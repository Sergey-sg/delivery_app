from django.conf.urls import include
from django.urls import path

from api.cart.views import CartItemListCreateAPIView, CustomerListCreateAPIView, OrderAPIView


urlpatterns = [
    path('detail/', CartItemListCreateAPIView.as_view(), name='cart_item_list_api'),
    path('customer/<int:pk>/', CustomerListCreateAPIView.as_view(), name='customer_detail_api'),
    path('order/', OrderAPIView.as_view(), name='order_list_api'),
]
