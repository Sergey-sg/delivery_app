from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from slugify import slugify

from shared.mixins.model_utils import CreatedUpdateMixins, ImageNameMixins
from shared.validators.validators import PHONE_REGEX


class Shop(CreatedUpdateMixins, ImageNameMixins):
    """
    Shop model
    attributes:
        name (str): name of shop
        slug (str): used to generate URL
        image (img): shop logo
        img_alt (str): text to be loaded in case of image loss
        phone (str): The phone number of shop
        email (str): shop email
        created (datetime): data of create shop
        updated (datetime): data of update shop
    """
    name = models.CharField(
        max_length=200,
        unique=True,
        validators=[MinLengthValidator(3)],
        verbose_name=_('name'),
        help_text=_('shop name')
    )
    slug = models.SlugField(
        unique=True,
        help_text=_('used to generate URL'),
        blank=True
    )
    image = models.ImageField(
        upload_to='logo/%Y/%m/%d',
        verbose_name=_('logo'),
        help_text=_('shop logo'),
        blank=True,
        null=True
    )
    img_alt = models.CharField(
        max_length=150,
        null=True, blank=True,
        verbose_name=_('image alternative'),
        help_text=_('text to be loaded in case of image loss')
    )
    phone = models.CharField(
        validators=[PHONE_REGEX],
        unique=True, max_length=13,
        verbose_name=_('phone number'),
        help_text=_('The phone number must be in the format: "+380999999999"')
    )
    email = models.EmailField(
        verbose_name=_('email'),
        help_text=_('shop email'),
        unique=True,
    )

    class Meta(object):
        verbose_name = _('shop')
        verbose_name_plural = _('Shops')
        ordering = ['-created']

    def __str__(self) -> str:
        """class method returns the shop in string representation"""
        return self.name

    def save(self, *args, **kwargs) -> None:
        """if the slug is not created then it is created from the name of the shop
        and rename image"""
        self.slug = slugify(self.slug or self.name)
        if self.image:
            field_name_image = self.get_current_image_name(model=Shop)
            if field_name_image['new']:
                self.image.name = field_name_image['image_name']
            if not self.img_alt and self.image:
                self.img_alt = self.name
        super(Shop, self).save(*args, **kwargs)


class Product(CreatedUpdateMixins, ImageNameMixins):
    """
    Product model
    attributes:
        shop (class Shop): communication with the Shop model
        name (str): name of product
        slug (str): used to generate URL
        description (str): product description
        price (float): the price of the product
        image (img): product image
        img_alt (str): text to be loaded in case of image loss
        stock (int): product quantity in stock
        available (bool): available product or not
        created (datetime): data of create product
        updated (datetime): data of update product
    """
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        verbose_name=_('shop'),
        help_text=_('shop to which the product belongs')
    )
    name = models.CharField(
        max_length=250,
        validators=[MinLengthValidator(3)],
        verbose_name=_('name'),
        help_text=_('product name')
    )
    slug = models.SlugField(
        unique=True,
        help_text=_('used to generate URL'),
        blank=True
    )
    description = models.TextField(
        verbose_name=_('description'),
        help_text=_('product description'),
        blank=True
    )
    price = models.DecimalField(
        verbose_name=_('price'),
        help_text=_('the price of the product'),
        max_digits=10,
        decimal_places=2
    )
    image = models.ImageField(
        upload_to='product/%Y/%m/%d',
        verbose_name=_('image'),
        help_text=_('product image'),
        blank=True,
        null=True
    )
    img_alt = models.CharField(
        max_length=150,
        null=True, blank=True,
        verbose_name=_('image alternative'),
        help_text=_('text to be loaded in case of image loss')
    )
    stock = models.IntegerField(
        verbose_name=_('stock'),
        help_text=_('product quantity in stock'),
        blank=True,
        null=True
    )
    available = models.BooleanField(
        verbose_name=_('available'),
        help_text=_('available product or not'),
        default=True
    )

    class Meta(object):
        verbose_name = _('product')
        verbose_name_plural = _('Products')
        ordering = ['shop']

    def __str__(self) -> str:
        """class method returns the product in string representation"""
        return self.name

    def save(self, *args, **kwargs) -> None:
        """if the slug is not created then it is created from the name of the product
        and rename image"""
        self.slug = slugify(self.slug or self.name)
        if self.image:
            field_name_image = self.get_current_image_name(model=Product)
            if field_name_image['new']:
                self.image.name = field_name_image['image_name']
            if not self.img_alt and self.image:
                self.img_alt = self.name
        super(Product, self).save(*args, **kwargs)
