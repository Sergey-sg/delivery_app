from django.test import TestCase
from django.urls import reverse_lazy

from apps.shop.models import Shop, Product


class CartTest(TestCase):

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

    def test_ProductListView(self):
        # test filtered queryset
        shop = Shop.objects.get(pk=1)
        resp = self.client.get(f"{reverse_lazy('home')}?filter_shop={shop.slug}")
        self.assertEquals(resp.status_code, 200)
        self.assertQuerysetEqual(
            resp.context['object_list'], Product.objects.filter(shop__slug=shop.slug), ordered=False
        )
        resp = self.client.get(reverse_lazy('home'))
        self.assertEquals(resp.status_code, 200)
        self.assertQuerysetEqual(resp.context['object_list'], Product.objects.all(), ordered=False)
