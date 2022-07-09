from django.urls import path

from apps.shop.views import ProductListView, CartView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('', CartView.as_view(), name='home'),
]
