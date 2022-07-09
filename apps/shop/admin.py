from django.contrib import admin

from apps.shop.models import Shop, Product


@admin.register(Shop)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'phone', 'email', 'created',)
    search_fields = ('name', 'phone')
    list_filter = ['created']


@admin.register(Product)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'shop', 'price', 'stock', 'available')
    search_fields = ('name', 'shop')
    list_filter = ['created']
