from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CreateCustomerOrderView.as_view(), name='cart_detail'),
    path('<int:product_id>/', include([
        path('add/', views.add_cart, name='add_cart'),
        path('remove/', views.cart_remove, name='cart_remove'),
        path('remove_product/', views.cart_remove_product, name='cart_remove_product'),
    ])),
    path('history-orders/', views.HistoryOrderListView.as_view(), name='history_orders')
]
