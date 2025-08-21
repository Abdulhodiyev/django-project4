from django.shortcuts import render

def about_page_view(request):
    return render(request, 'about.html')

def n404_page_view(request):
    return render(request, '404.html')

def blog_detail_page_view(request):
    return render(request, 'blog-detail.html')

def blog_list_page_view(request):
    return render(request, 'blog-list.html')

def cart_page_view(request):
    return render(request, 'cart.html')

def category_page_view(request):
    return render(request, 'category.html')

def checkout_page_view(request):
    return render(request, 'checkout.html')

def contact_page_view(request):
    return render(request, 'contact.html')

def dashboard_page_view(request):
    return render(request, 'dashboard.html')

def faq_page_view(request):
    return render(request, 'faq.html')

def login_page_view(request):
    return render(request, 'login.html')

def product_detail_page_view(request):
    return render(request, 'product-detail.html')

def wishlist_page_view(request):
    return render(request, 'wishlist.html')