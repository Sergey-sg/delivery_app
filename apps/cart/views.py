from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView
from django_filters.views import FilterView

from apps.cart.filters import OrderFilter
from apps.cart.forms import CustomerForm
from apps.cart.models import Cart, CartItem, Customer, Order
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


class CreateCustomerOrderView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'cart/customer_order_form.jinja2'

    def get_context_data(self, total=0, counter=0, cart_items=0, **kwargs):
        context = super(CreateCustomerOrderView, self).get_context_data(**kwargs)
        try:
            cart = Cart.objects.get(cart_id=_cart_id(self.request))
            context['cart_items'] = CartItem.objects.filter(cart=cart, active=True)
            context['total'] = total
            context['counter'] = counter
            for cart_item in context['cart_items']:
                context['total'] += (cart_item.product.price * cart_item.quantity)
                context['counter'] = cart_item.quantity
        except ObjectDoesNotExist:
            pass
        return context

    def post(self, request, *args, **kwargs):
        """checks valid of filling out the class form"""
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, *args, **kwargs):
        """save class form"""
        customer_form = form.save(commit=False)
        try:
            customer = Customer.objects.get(
                name=customer_form.name, email=customer_form.email,
                phone=customer_form.phone, address=customer_form.address
            )
        except Customer.DoesNotExist:
            customer_form.save()
            customer = customer_form
        cart = Cart.objects.get(cart_id=_cart_id(self.request))
        cart_items = CartItem.objects.filter(cart=cart)
        order = Order.objects.create(customer=customer, total_price=self.request.POST.get('total_price'))
        for cart_item in cart_items:
            cart_item.active = False
            cart_item.order = order
            if cart_item.product.stock:
                cart_item.product.stock -= cart_item.quantity
                cart_item.product.save()
            cart_item.save()
        cart.delete()
        return render(self.request, 'cart/successful_order.jinja2', context={'order': order.pk})


class HistoryOrderListView(FilterView):
    """
    Generates a list of orders filtered by email and phone
    """
    template_name = 'shop/home.jinja2'
    filterset_class = OrderFilter

    def get_queryset(self):
        """return queryset with filter"""
        if 'filter_shop' in self.request.GET and self.request.GET['filter_shop']:
            qs = qs.filter(shop__slug=self.request.GET['filter_shop'])
        return qs

    def get_context_data(self, **kwargs: dict) -> dict:
        """Add to context filter as "filterset" """
        context = super(ProductListView, self).get_context_data()
        context['filterset'] = self.filterset
        context['shops'] = Shop.objects.all()
        return context
