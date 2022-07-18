from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_google_maps import fields as map_fields

from apps.shop.models import Product
from shared.mixins.model_utils import CreatedUpdateMixins
from shared.validators.validators import PHONE_REGEX


class Cart(CreatedUpdateMixins):
    """
    Cart model
    attributes:
        cart_id (str): id cart for current session (generated automatically)
        created (datetime): data of create comment
        updated (datetime): data of update comment
    """
    cart_id = models.CharField(max_length=250, blank=True)

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('Carts')
        ordering = ['-created']

    def __str__(self) -> str:
        """class method returns the cart_id in string representation"""
        return self.cart_id


class CartItem(models.Model):
    """
    CartItem model
    attributes:
        product (class Product): communication with the Product model
        cart (class Cart): communication with the Cart model
        order (class Order): communication with the Order model
        quantity (int): the quantity of the product in the cart
        active (bool): indicator of the state of the cart item (true - in the cart, false - the order is placed)
        sub_total (float): the total price of the products in cart item
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('product'),
        help_text=_('communication with the Product model')
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('cart'),
        help_text=_('communication with the Cart model')
    )
    order = models.ForeignKey(
        'Order',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('order'),
        help_text=_('communication with the Order model')
    )
    quantity = models.IntegerField(
        verbose_name=_('quantity'),
        help_text=_('the quantity of the product in the cart item')
    )
    active = models.BooleanField(
        default=True,
        verbose_name=_('active'),
        help_text=_('indicator of the state of the cart item')
    )
    sub_total = models.DecimalField(
        verbose_name=_('sub_total'),
        help_text=_('the total price of the products in cart item'),
        max_digits=12,
        decimal_places=2
    )

    class Meta:
        verbose_name = _('cart item')
        verbose_name_plural = _('Cart Items')

    def __str__(self) -> str:
        """class method returns the CartItem in string representation"""
        return self.product.name

    def save(self, *args, **kwargs) -> None:
        """saves the total amount for the product"""
        self.sub_total = self.product.price * self.quantity
        super(CartItem, self).save(*args, **kwargs)


class Customer(models.Model):
    """
    Customer model
    attributes:
        name (str): customer name
        email (str): email customer, used for feedback
        phone (str): phone number, used for feedback
        address (str): customer address for delivery
        geolocation (str): geolocation of the customer, used to adjust the delivery location
    """
    name = models.CharField(
        max_length=250,
        validators=[MinLengthValidator(2)],
        verbose_name=_('name'),
        help_text=_('customer name')
    )
    email = models.EmailField(
        verbose_name=_('email'),
        help_text=_('used for feedback'),
    )
    phone = models.CharField(
        validators=[PHONE_REGEX],
        max_length=13,
        verbose_name=_('phone number'),
        help_text=_('used for feedback')
    )
    address = map_fields.AddressField(
        max_length=200,
        verbose_name=_('address'),
        help_text=_('address for delivery')
    )
    geolocation = map_fields.GeoLocationField(
        max_length=100,
        verbose_name=_('geolocation'),
        help_text=_('geolocation of the customer')
    )

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('Customers')

    def __str__(self) -> str:
        """class method returns the Customer in string representation"""
        return self.name


class Order(CreatedUpdateMixins):
    """
    Order model
    attributes:
        customer (class Customer): communication with the Customer model
        sent (bool): order dispatch status
        total_price (float): total price of order
        created (datetime): data of create comment
        updated (datetime): data of update comment
    """
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('customer'),
        help_text=_('communication with the Customer model')
    )
    sent = models.BooleanField(
        default=False,
        verbose_name=_('sent'),
        help_text=_('order dispatch status')
    )
    total_price = models.DecimalField(
        verbose_name=_('total price'),
        help_text=_('total price of order'),
        max_digits=12,
        decimal_places=2
    )

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('Orders')

    def __str__(self) -> str:
        """class method returns the Order in string representation"""
        if len(f'{self.pk}') < 4:
            out = f"{(4-len(str(self.pk)))*'0'}{self.pk}"
            return out
        else:
            return self.pk
