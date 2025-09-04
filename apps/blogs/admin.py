from django.contrib import admin

from apps.blogs.models import BlogCategoryModel, BlogTagModel, BlogAuthorModel, BlogListModel, BlogViewModel


@admin.register(BlogCategoryModel)
class BlogCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(BlogTagModel)
class BlogTagModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(BlogAuthorModel)
class BlogAuthorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    search_fields = ['full_name']
    list_filter = ['created_at']
    ordering = ['-id']


@admin.register(BlogListModel)
class BlogListModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['created_at', 'status']


@admin.register(BlogViewModel)
class BlogViewModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_ip', 'blog__title', 'created_at']
    search_fields = ['user_ip']
    list_filter = ['created_at', 'user_ip']