from django.db.models import QuerySet
from django.views.generic import DetailView
from django_filters.views import FilterView

from apps.shop.filters import ProductFilter
from apps.shop.models import Shop, Product


class ProductListView(FilterView):
    """
    Generates a list of product with filter
    """
    template_name = 'shop/home.jinja2'
    filterset_class = ProductFilter
    model = Product
    paginate_by = 10

    def get_queryset(self) -> QuerySet:
        """return queryset with filter"""
        qs = super(ProductListView, self).get_queryset()
        if 'filter_shop' in self.request.GET and self.request.GET['filter_shop']:
            qs = qs.filter(shop__slug=self.request.GET['filter_shop'])
        return qs

    def get_context_data(self, **kwargs: dict) -> dict:
        """Add to context filter as "filterset" and shops"""
        context = super(ProductListView, self).get_context_data()
        context['filterset'] = self.filterset
        context['shops'] = Shop.objects.all()
        return context


class ProductDetailView(DetailView):
    """Returns a detailed view of the product"""
    model = Product
    template_name = 'shop/product_detail.jinja2'
