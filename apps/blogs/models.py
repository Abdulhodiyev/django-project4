from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class BaseBlogModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlogAuthorModel(BaseBlogModel):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='authors/')
    bio = models.CharField(max_length=256)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class BlogCategoryModel(BaseBlogModel):
    title = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class BlogTagModel(BaseBlogModel):
    title = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class BlogListModel(BaseBlogModel):
    class BlogStatus(models.TextChoices):
        DRAFT = 'DRAFT'
        PUBLISHED ='PUBLISHED'
        DELETED = 'DELETED'

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blogs')
    description = RichTextUploadingField
    status = models.CharField(max_length=20, choices=BlogStatus, default=BlogStatus.DRAFT)

    categories = models.ManyToManyField(
        BlogCategoryModel,
        related_name='blogs'
    )

    author_by = models.ForeignKey(
        BlogAuthorModel,
        on_delete=models.CASCADE,
        related_name='author'
    )

    tags = models.ManyToManyField(
        BlogTagModel,
        related_name='tag'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
