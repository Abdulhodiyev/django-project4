from django.urls import path

from apps.pages.views import home_page_view, n404_view, about_view, coming_soon_view, faq_view, contact_view

app_name = 'pages'

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('faq/', faq_view, name='faq'),
    path('coming-soon/', coming_soon_view, name='coming-soon'),
    path('about/', about_view, name='about'),
    path('404/', n404_view, name='404'),
    path('', home_page_view, name='home')
]