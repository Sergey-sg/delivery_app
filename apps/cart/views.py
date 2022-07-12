from typing import Dict, Any

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet, Sum
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView, ListView

from apps.cart.forms import CustomerForm
from apps.cart.models import Cart, CartItem, Customer, Order
from apps.shop.models import Product
from shared.mixins.views_mixins import get_cart_id, moving_products_from_cart_to_order


def add_cart_item_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
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
    return redirect(request.META.get('HTTP_REFERER'))


def cart_item_update_quantity(request, product_id):
    cart = Cart.objects.get(cart_id=get_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_detail')


def cart_item_delete(request, product_id):
    cart = Cart.objects.get(cart_id=get_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_detail')


class CreateCustomerOrderView(CreateView):
    """displays the contents of the cart, creates a customer and saves the order"""
    model = Customer
    form_class = CustomerForm
    template_name = 'cart/customer_order_form.jinja2'

    def get_context_data(self, total=0, cart_items=0, **kwargs) -> Dict[str, Any]:
        """inserts the total value of the cart and the items in the cart into context"""
        context = super(CreateCustomerOrderView, self).get_context_data(**kwargs)
        try:
            cart = Cart.objects.get(cart_id=get_cart_id(self.request))
            cart_items = CartItem.objects.filter(cart=cart, active=True)
            total = cart_items.aggregate(Sum('sub_total'))['sub_total__sum']
        except ObjectDoesNotExist:
            pass
        context['cart_items'] = cart_items
        context['total'] = float(total)
        return context

    def post(self, request, *args, **kwargs) -> HttpResponse:
        """checks valid of filling out the class form"""
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, *args, **kwargs) -> HttpResponse:
        """saves the form and redirects to the successful order page"""
        customer_form = form.save(commit=False)
        try:
            customer = Customer.objects.get(
                name=customer_form.name, email=customer_form.email,
                phone=customer_form.phone, address=customer_form.address
            )
        except Customer.DoesNotExist:
            customer_form.save()
            customer = customer_form
        order_id = moving_products_from_cart_to_order(request=self.request, customer=customer)
        return render(self.request, 'cart/successful_order.jinja2', context={'order': order_id})


class HistoryOrderListView(ListView):
    """
    Generates a list of orders filtered by email and phone
    """
    template_name = 'cart/history_orders.jinja2'

    def get_queryset(self) -> QuerySet[Order]:
        """return queryset with filter"""
        if 'email' and 'phone' in self.request.GET and self.request.GET['email'] and self.request.GET['phone']:
            return Order.objects.filter(customer__email=self.request.GET['email'],
                                        customer__phone=self.request.GET['phone'])
        elif 'email' in self.request.GET and self.request.GET['email']:
            return Order.objects.filter(customer__email=self.request.GET['email'])
        elif 'phone' in self.request.GET and self.request.GET['phone']:
            return Order.objects.filter(customer__phone=self.request.GET['phone'])
