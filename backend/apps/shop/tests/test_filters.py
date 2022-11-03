from django.test import TestCase

from apps.shop.filters import ProductFilter
from apps.shop.models import Shop, Product


class ProductFilterTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        for shop_num in range(3):
            shop = Shop.objects.create(
                name=f'shop{shop_num}', phone=f'+38084057837{shop_num}', email=f'email{shop_num}@shop.com'
            )
            for product_num in range(3):
                Product.objects.create(
                    shop=shop, name=f'product{product_num}shop{shop_num}',
                    description='product description', price=34.5, stock=66
                )

    def test_str_method(self):
        queryset = Product.objects.all()
        shop = Shop.objects.get(pk=1)
        filtered_queryset = ProductFilter.filter_shop(queryset, name='', value=[shop.slug])
        self.assertQuerysetEqual(filtered_queryset, queryset.filter(shop__slug=shop.slug), ordered=False)
        filtered_queryset = ProductFilter.filter_shop(queryset, name='', value=['shop.slug'])
        self.assertQuerysetEqual(filtered_queryset, queryset.filter(shop__slug='shop.slug'), ordered=False)
