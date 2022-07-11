from django.contrib import admin

from apps.cart.models import Customer, Cart, CartItem, Order


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'created',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'order', 'quantity', 'active',)


class CartItemInlineAdmin(admin.TabularInline):
    model = CartItem
    # list_display = ('product', 'quantity')
    exclude = ['active', 'cart']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'sent', 'total_price', 'created',)
    inlines = [CartItemInlineAdmin]
