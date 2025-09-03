from django.shortcuts import render

from apps.blogs.models import BlogListModel, BlogCategoryModel, BlogTagModel


def blog_list_view(request):
    blogs = BlogListModel.objects.filter(
        status=BlogListModel.BlogStatus.PUBLISHED
    )
    categories = BlogCategoryModel.objects.all()
    tags = BlogTagModel.objects.all()
    context = {
        'blogs': blogs,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'blogs/blog-list.html', context)

def blog_detail_view(request, pk):
    try:
        blog = BlogListModel.objects.get(id=pk)
    except BlogListModel.DoesNotExists:
        return render(request, 'pages/404.html')
    categories = BlogCategoryModel.objects.all()
    tags = BlogTagModel.objects.all()
    context = {
        "blog": blog,
        'categories': categories,
        'tags': tags,
    }
    return render(
        request, 'blogs/blog-detail.html',
        context
    )