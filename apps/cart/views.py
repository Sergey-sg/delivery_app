from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView

from apps.cart.forms import CustomerForm
from apps.cart.models import Cart, CartItem, Customer
from apps.shop.models import Product


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
    cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()
    return redirect(request.META.get('HTTP_REFERER'))


def cart_detail(request, total=0, counter=0, cart_items=0):
    form = CustomerForm()
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter = cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(
        request,
        'cart/cart.jinja2', dict(cart_items=cart_items, total=total, counter=counter, form=form)
    )


def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_detail')


def cart_remove_product(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_detail')


class CreateCustomerView(CreateView):
    model = Customer
    form_class = CustomerForm

    # def post(self, request, *args, **kwargs):
    #     """checks valid of filling out the class form"""
    #     self.object = None
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    def form_valid(self, form, *args):
        """save class form"""
        object_form = form.save(commit=False)
        object_form.cart = Cart.objects.get(cart_id=_cart_id(self.request))
        object_form.save()
        return render(self.request, 'cart/successful_order.jinja2')
