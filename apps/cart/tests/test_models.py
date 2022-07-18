from django.test import TestCase

from apps.cart.models import Cart, CartItem, Customer, Order
from apps.shop.models import Product, Shop


class CartModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Cart.objects.create(cart_id='drjdtyjftyjyutfkyukyuk')

    def test_str_method(self):
        cart = Cart.objects.get(pk=1)
        field_id = cart.cart_id
        self.assertEquals(field_id, cart.__str__())


class CartItemModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cart = Cart.objects.create(cart_id='drjdtyjftyjyutfkyukyuk')
        shop = Shop.objects.create(name='shop', phone='+380840578373', email='email@shop.com',)
        product = Product.objects.create(
            shop=shop, name='product', description='product description', price=34.5, stock=66
        )
        CartItem.objects.create(product=product, cart=cart, quantity=3)

    def test_str_method(self):
        cart_item = CartItem.objects.get(pk=1)
        field_id = cart_item.product.name
        self.assertEquals(field_id, cart_item.__str__())

    def test_sub_total_in_save(self):
        cart_item = CartItem.objects.get(pk=1)
        sub_total = cart_item.quantity * cart_item.product.price
        self.assertEqual(sub_total, cart_item.sub_total)


class CustomerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Customer.objects.create(
            name='customer',
            email='test@gmail.com',
            phone='+380678574738',
            address='Запорожье, Запорожская область, Украина',
            geolocation='47.8388,35.139567'
        )

    def test_str_method(self):
        customer = Customer.objects.get(pk=1)
        field_name = customer.name
        self.assertEquals(field_name, customer.__str__())


class OrderModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        customer = Customer.objects.create(
            name='customer',
            email='test@gmail.com',
            phone='+380678574738',
            address='Запорожье, Запорожская область, Украина',
            geolocation='47.8388,35.139567'
        )
        Order.objects.create(
            customer=customer,
            total_price=45
        )

    def test_str_method(self):
        order = Order.objects.get(pk=1)
        self.assertEquals(f'000{order.pk}', order.__str__())

    def test_str_method_after_999(self):
        order = Order.objects.create(
            pk=1000,
            customer=Customer.objects.get(pk=1),
            total_price=45
        )
        self.assertEquals(order.pk, order.__str__())
