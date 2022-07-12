from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CreateCustomerOrderView.as_view(), name='cart_detail'),
    path('<int:product_id>/', include([
        path('add/', views.add_cart_item_to_cart, name='add_cart'),
        path('remove/', views.cart_item_update_quantity, name='cart_remove'),
        path('remove_product/', views.cart_item_delete, name='cart_remove_product'),
    ])),
    path('history-orders/', views.HistoryOrderListView.as_view(), name='history_orders')
]
