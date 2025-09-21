from django.urls import path

from apps.pages.views import home_page_view, about_view, contact_view

app_name = 'pages'

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('', home_page_view, name='home'),
]