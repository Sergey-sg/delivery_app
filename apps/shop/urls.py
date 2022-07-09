from django.urls import path

from apps.shop.views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
]
