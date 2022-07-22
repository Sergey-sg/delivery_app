from django.urls import path

from apps.shop.views import ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product_detail'),
]
