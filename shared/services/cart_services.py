from django.db.models import Sum

from apps.cart.models import Cart, CartItem, Order
from shared.mixins.views_mixins import get_cart_id


def cart_item_create_or_add_quantity(product, request):
    try:
        cart = Cart.objects.get(cart_id=get_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=get_cart_id(request))
    cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()


def reduce_quantity_of_cart_item_or_delete(product, request):
    cart = Cart.objects.get(cart_id=get_cart_id(request))
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()


def cart_item_delete(product, request):
    cart = Cart.objects.get(cart_id=get_cart_id(request))
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()


def moving_products_from_cart_to_order(request, customer) -> str:
    """moving products from cart to order and deleting cart"""
    cart = Cart.objects.get(cart_id=get_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart)
    total = cart_items.aggregate(Sum('sub_total'))['sub_total__sum']
    order = Order.objects.create(customer=customer, total_price=total)
    for cart_item in cart_items:
        cart_item.active = False
        cart_item.order = order
        if cart_item.product.stock:
            cart_item.product.stock -= cart_item.quantity
            cart_item.product.save()
        cart_item.save()
    cart.delete()
    return order.__str__()
