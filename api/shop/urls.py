from django.conf.urls import include
from django.urls import path

from api.shop.views import ProductDetailAPIView, ProductListAPIView, ShopListAPIView


urlpatterns = [
    path('v1/', include([
        path('product/', include([
            path('list/', ProductListAPIView.as_view(), name='products_list_api'),
            path('<slug:slug>/', ProductDetailAPIView.as_view(), name='product_detail_api'),
        ])),
        path('shops/', ShopListAPIView.as_view(), name='shops_list_api'),
    ])),
]
