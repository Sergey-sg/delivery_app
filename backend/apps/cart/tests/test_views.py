from django.test import TestCase
from django.urls import reverse_lazy

from apps.cart.models import CartItem, Customer, Order
from apps.shop.models import Shop, Product


class CartTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        shop = Shop.objects.create(name='shop', phone='+380840578373', email='email@shop.com', )
        Product.objects.create(shop=shop, name='product', description='product description', price=34.5, stock=66)

    def test_AddCartItemToCart(self):
        # test add product to cart item
        referer = reverse_lazy('home')
        resp = self.client.get(reverse_lazy('add_cart', kwargs={'pk': 1}), HTTP_REFERER=referer)
        self.assertEqual(CartItem.objects.get(pk=1).quantity, 1)
        self.assertRedirects(resp, reverse_lazy('home'))
        # test increasing the amount of product in cart item without HTTP_REFERER
        resp = self.client.get(reverse_lazy('add_cart', kwargs={'pk': 1}))
        self.assertRedirects(resp, reverse_lazy('home'))
        self.assertEqual(CartItem.objects.get(pk=1).quantity, 1)
        # test increasing the amount of product in cart item with HTTP_REFERER
        resp = self.client.get(reverse_lazy('add_cart', kwargs={'pk': 1}), HTTP_REFERER=referer)
        self.assertEqual(CartItem.objects.get(pk=1).quantity, 2)

    def test_CartItemReduceQuantityOrDelete(self):
        # test reduce product quantity in cart item
        referer = reverse_lazy('cart_detail')
        for item in range(3):
            self.client.get(reverse_lazy('add_cart', kwargs={'pk': 1}), HTTP_REFERER=referer)
        self.assertEqual(CartItem.objects.get(pk=1).quantity, 3)
        resp = self.client.get(reverse_lazy('cart_remove', kwargs={'pk': 1}), HTTP_REFERER=referer)
        self.assertEqual(CartItem.objects.get(pk=1).quantity, 2)
        self.assertRedirects(resp, reverse_lazy('cart_detail'))
        # test reduce product quantity in cart item without HTTP_REFERER
        resp = self.client.get(reverse_lazy('cart_remove', kwargs={'pk': 1}))
        self.assertRedirects(resp, reverse_lazy('home'))
        self.assertEqual(CartItem.objects.get(pk=1).quantity, 2)
        # test product quantity reduction to remove product in cart using HTTP_REFERER
        for item in range(2):
            self.client.get(reverse_lazy('cart_remove', kwargs={'pk': 1}), HTTP_REFERER=referer)
        self.assertEqual(CartItem.objects.filter(pk=1).count(), 0)

    def test_CartItemDelete(self):
        # test delete a product from a cart item
        referer = reverse_lazy('cart_detail')
        for item in range(3):
            self.client.get(reverse_lazy('add_cart', kwargs={'pk': 1}), HTTP_REFERER=referer)
        self.assertEqual(CartItem.objects.get(pk=1).quantity, 3)
        # test delete a product from a cart item without HTTP_REFERER
        resp = self.client.get(reverse_lazy('cart_remove_product', kwargs={'pk': 1}))
        self.assertRedirects(resp, reverse_lazy('home'))
        self.assertEqual(CartItem.objects.get(pk=1).quantity, 3)
        # test delete a product from a cart item with HTTP_REFERER
        resp = self.client.get(reverse_lazy('cart_remove_product', kwargs={'pk': 1}), HTTP_REFERER=referer)
        self.assertRedirects(resp, reverse_lazy('cart_detail'))
        self.assertEqual(CartItem.objects.filter(pk=1).count(), 0)

    def test_CreateCustomerOrderView(self):
        referer = reverse_lazy('cart_detail')
        resp = self.client.get(reverse_lazy('cart_detail'))
        self.assertEqual(resp.status_code, 200)
        for item in range(5):
            self.client.get(reverse_lazy('add_cart', kwargs={'pk': 1}), HTTP_REFERER=referer)
        resp = self.client.get(reverse_lazy('cart_detail'))
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post(
            reverse_lazy('cart_detail'),
            data={
                'name': 'customer name',
                'email': 'order@customer.com',
                'phone': '+380583763743',
                'address': 'ул. Рабочая, 36, Днепр, Днепропетровская область, Украина',
                'geolocation': '48.4622234,35.0075235',
                  }
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Customer.objects.get(pk=1).email, 'order@customer.com')
        self.assertEqual(Order.objects.get(pk=1).total_price, 34.5*5)

    def test_HistoryOrderListView(self):
        resp = self.client.get(reverse_lazy('history_orders'))
        self.assertEqual(resp.status_code, 200)
        referer = reverse_lazy('cart_detail')
        # created order and customer
        for item in range(3):
            self.client.get(reverse_lazy('add_cart', kwargs={'pk': 1}), HTTP_REFERER=referer)
            self.client.post(
                reverse_lazy('cart_detail'),
                data={
                    'name': 'customer name',
                    'email': f'{item}order@customer.com',
                    'phone': '+380583763743',
                    'address': 'ул. Рабочая, 36, Днепр, Днепропетровская область, Украина',
                    'geolocation': '48.4622234,35.0075235',
                }
            )
        # test filter order with current email
        resp = self.client.get(f"{reverse_lazy('history_orders')}?email=1order@customer.com")
        self.assertQuerysetEqual(resp.context['object_list'],
                                 Order.objects.filter(customer__email='1order@customer.com'))
        # filter testing with non-existent email
        resp = self.client.get(f"{reverse_lazy('history_orders')}?email=5order@customer.com")
        self.assertEqual(resp.context['object_list'].count(), 0)
        # filter testing with phone
        resp = self.client.get(f"{reverse_lazy('history_orders')}?email=&phone=%2B380583763743")
        self.assertQuerysetEqual(resp.context['object_list'],
                                 Order.objects.filter(customer__phone='+380583763743'), ordered=False)
        self.assertEqual(resp.context['object_list'].count(), 3)
        # filter testing with phone and email
        resp = self.client.get(f"{reverse_lazy('history_orders')}?email=1order@customer.com&phone=%2B380583763743")
        self.assertQuerysetEqual(
            resp.context['object_list'],
            Order.objects.filter(customer__phone='+380583763743').filter(customer__email='1order@customer.com'),
            ordered=False
        )
        self.assertEqual(resp.context['object_list'].count(), 1)


