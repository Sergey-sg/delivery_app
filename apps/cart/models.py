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
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('cart item')
        verbose_name_plural = _('Cart Items')

    def __str__(self):
        return self.product

    def sub_total(self):
        return self.product.price * self.quantity


class Customer(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
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
