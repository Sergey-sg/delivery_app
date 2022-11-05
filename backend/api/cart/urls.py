from django.conf.urls import include
from django.urls import path

# from api.cart.views import CartItemListCreateAPIView, CustomerDetailAPIView, OrderAPIView, CustomerListCreateAPIView, OrderDetailUpdateAPIView


# urlpatterns = [
#     path('detail/', CartItemListCreateAPIView.as_view(), name='cart_item_list_api'),
#     path('customer/', include([
#         path('', CustomerListCreateAPIView.as_view(), name='customer_list_api'),
#         path('<int:pk>/', CustomerDetailAPIView.as_view(), name='customer_detail_api'),
#     ])),
#     path('order/', include([
#         path('', OrderAPIView.as_view(), name='order_list_api'),
#         path('<int:pk>', OrderDetailUpdateAPIView.as_view(), name='order_detail_api'),
#     ])),
# ]
