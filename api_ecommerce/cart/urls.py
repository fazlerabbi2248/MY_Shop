from django.urls import path
from .views import CartDetailView, CartItemCreateView, CartItemUpdateView, CartItemDeleteView

urlpatterns = [
    path('cart/', CartDetailView.as_view(), name='cart-detail'),
    path('cart/add/', CartItemCreateView.as_view(), name='cart-item-create'),
    path('cart/<int:pk>/update/', CartItemUpdateView.as_view(), name='cart-item-update'),
    path('cart/<int:pk>/delete/', CartItemDeleteView.as_view(), name='cart-item-delete'),

]
