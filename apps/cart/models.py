from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shop.models import Product
from shared.mixins.model_utils import CreatedUpdateMixins
from shared.validators.validators import PHONE_REGEX


class Cart(CreatedUpdateMixins):
    cart_id = models.CharField(max_length=250, blank=True)

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('Carts')
        ordering = ['-created']

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('cart item')
        verbose_name_plural = _('Cart Items')

    def __str__(self):
        return self.product.name

    def sub_total(self):
        return self.product.price * self.quantity


class Customer(models.Model):
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
    address = models.CharField(
        max_length=500,
        verbose_name=_('address'),
        help_text=_('shipping address')
    )

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('Customers')

    def __str__(self):
        return self.name


class Order(CreatedUpdateMixins):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    sent = models.BooleanField(default=False)
    total_price = models.DecimalField(
        verbose_name=_('total price'),
        help_text=_('total price of order'),
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        if len(f'{self.pk}') < 4:
            return f'000{self.pk}'
        else:
            return self.pk

