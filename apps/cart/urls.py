from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CreateCustomerOrderView.as_view(), name='cart_detail'),
    path('<int:pk>/', include([
        path('add/', views.AddCartItemToCart.as_view(), name='add_cart'),
        path('remove/', views.CartItemReduceQuantityOrDelete.as_view(), name='cart_remove'),
        path('remove_product/', views.CartItemDelete.as_view(), name='cart_remove_product'),
    ])),
    path('history-orders/', views.HistoryOrderListView.as_view(), name='history_orders')
]
