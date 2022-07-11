from django_filters import rest_framework as filters

from apps.shop.models import Product


class ProductFilter(filters.FilterSet):
    """filter for Product"""

    class Meta:
        model = Product
        fields = ('shop', 'name',)

    @staticmethod
    def filter_shop(queryset, name, value):
        """get the filter value by shop and return queryset of product"""
        try:
            products = Product.objects.filter(shop__slug=value[0], available=True)
            return products
        except Exception:
            pass
        return queryset
