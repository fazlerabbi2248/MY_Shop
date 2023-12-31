from rest_framework import generics
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.permissions import IsAuthenticated

class CartDetailView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_cart, created = Cart.objects.get_or_create(user=self.request.user)
        return user_cart

class CartItemCreateView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user_cart, created = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=user_cart)

class CartItemUpdateView(generics.UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

class CartItemDeleteView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
