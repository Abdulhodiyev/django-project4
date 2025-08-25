from django.urls import path

from apps.blogs.views import blog_list_view, blog_detail_view

app_name = 'blogs'

urlpatterns = [
    path('blog-detail/', blog_detail_view, name='detail'),
    path('', blog_list_view, name='list'),
]