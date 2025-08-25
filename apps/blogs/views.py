from django.shortcuts import render

def blog_list_view(request):
    return render(request, 'blogs/blog-list.html')

def blog_detail_view(request):
    return render(request, 'blogs/blog-detail.html')