from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('categorieslist/', views.CategoryList.as_view(), name='category-list'),
    path('productscreate/', views.ProductCreate.as_view(), name='product-create'),
    path('products/<int:pk>/update/', views.ProductUpdate.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('products/search/', views.ProductSearchView.as_view(), name='product-search'),
    path('products/<int:product_id>/reviews/', views.ReviewListByProduct.as_view(), name='product_reviews'),
    path('products/reviews/create/', views.ReviewCreate.as_view(), name='review-create'),
    path('products/reviews/<int:pk>/update/', views.ReviewUpdate.as_view(), name='update_review'),
    path('products/reviews/<int:pk>/delete/', views.ReviewDelete.as_view(), name='delete_review'),

]