from django.urls import path

from apps.pages.views import about_page_view, n404_page_view, blog_detail_page_view, blog_list_page_view, cart_page_view, category_page_view, checkout_page_view, contact_page_view, dashboard_page_view, faq_page_view, login_page_view, product_detail_page_view, wishlist_page_view

app_name = 'pages'

urlpatterns = [
    path('wishlist/', wishlist_page_view, name='wishlist'),
    path('product-detail/', product_detail_page_view, name='product-detail'),
    path('login/', login_page_view, name='login'),
    path('faq/', faq_page_view, name='faq'),
    path('dashboard/', dashboard_page_view, name='dashboard'),
    path('contact/', contact_page_view, name='contact'),
    path('checkout/', checkout_page_view, name='checkout'),
    path('category/', category_page_view, name='category'),
    path('cart/', cart_page_view, name='cart'),
    path('blog-list/', blog_list_page_view, name='blog-list'),
    path('blog-detail/', blog_detail_page_view, name='blog-detail'),
    path('about/', about_page_view, name='about'),
    path('404/', n404_page_view, name='404'),
]