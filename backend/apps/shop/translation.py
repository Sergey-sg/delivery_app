from modeltranslation.translator import translator, TranslationOptions

from apps.shop.models import Shop, Product


class ShopTranslationOptions(TranslationOptions):
    fields = ('name', 'img_alt')


class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'img_alt')


translator.register(Shop, ShopTranslationOptions)
translator.register(Product, ProductTranslationOptions)
