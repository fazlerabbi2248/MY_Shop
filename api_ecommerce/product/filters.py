import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category', lookup_expr='icontains')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    price = django_filters.NumberFilter(field_name='price')
    available_stock = django_filters.NumberFilter(field_name='available_stock')

    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'available_stock']