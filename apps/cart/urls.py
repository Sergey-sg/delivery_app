from django.urls import path, include
from . import views

urlpatterns = [
    path('', include([
        path('', views.cart_detail, name='cart_detail'),
        path('<int:product_id>/', include([
            path('add/', views.add_cart, name='add_cart'),
            path('remove/', views.cart_remove, name='cart_remove'),
            path('remove_product/', views.cart_remove_product, name='cart_remove_product'),
        ]))
    ])),
    path('customer/', views.CreateCustomerView.as_view(), name='customer')
]
