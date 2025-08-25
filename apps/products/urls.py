from django.urls import path

from apps.products.views import products_view, cart_view, category_view, checkout_view, wishlist_view

app_name = 'products'

urlpatterns = [
    path('wishlist/', wishlist_view, name='wishlist'),
    path('checkout/', checkout_view, name='checkout'),
    path('category/', category_view, name='category'),
    path('cart/', cart_view, name='cart'),
    path('', products_view, name='dashboard'),
]
