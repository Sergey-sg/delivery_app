from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from apps.shop.models import Shop, Product


class ShopModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Shop.objects.create(
            name='shop', phone='+380840578371', email='email@shop.com'
        )

    def test_str_method(self):
        shop = Shop.objects.get(pk=1)
        field_name = shop.name
        self.assertEquals(field_name, shop.__str__())

    def test_load_logo(self):
        # test load new logo
        shop = Shop.objects.get(pk=1)
        logo = SimpleUploadedFile(
            name='test_image.jpg',
            content=open('static/media/user_photo/default_user_photo.png', 'rb').read(),
            content_type='image/jpeg'
        )
        shop.image = logo
        shop.save()
        self.assertIn(shop.name, shop.image.name)
        self.assertEquals(shop.img_alt, shop.name)
        # test load new logo for new shop (shop.pk == None)
        shop = Shop()
        shop.name = 'new-shop'
        shop.email = 'new-email@shop.com'
        shop.phone = '+380840578372'
        shop.image = logo
        shop.save()
        self.assertIn(shop.name, shop.image.name)
        self.assertEquals(shop.img_alt, shop.name)
        # test not load new logo
        shop.save()
        self.assertIn(shop.name, shop.image.name)
        self.assertEquals(shop.img_alt, shop.name)


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        shop = Shop.objects.create(name='shop', phone='+380840578371', email='email@shop.com')
        Product.objects.create(shop=shop, name='product', description='product description', price=34.5, stock=66)

    def test_str_method(self):
        product = Product.objects.get(pk=1)
        field_name = product.name
        self.assertEquals(field_name, product.__str__())

    def test_load_image(self):
        product = Product.objects.get(pk=1)
        image = SimpleUploadedFile(
            name='test_image.jpg',
            content=open('static/media/user_photo/default_user_photo.png', 'rb').read(),
            content_type='image/jpeg'
        )
        product.image = image
        product.save()
        self.assertIn(product.name, product.image.name)
        self.assertEquals(product.img_alt, product.name)
