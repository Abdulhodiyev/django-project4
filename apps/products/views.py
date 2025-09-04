from django.shortcuts import render


def products_view(request):
    return render(request, 'products/product-detail.html')

def cart_view(request):
    return render(request, 'products/cart.html')

def category_view(request):
    return render(request, 'products/category.html')

def checkout_view(request):
    return render(request, 'products/checkout.html')

def wishlist_view(request):
    return render(request, 'products/wishlist.html')