from django.db import models


class BaseBlogModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlogAuthorModel(BaseBlogModel):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='authors/')
    bio = models.TextField()

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
    STATUS_CHOICES = (
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blogs')
    description = models.TextField()

    categories = models.ManyToManyField(
        BlogCategoryModel,
        related_name='blogs'
    )

    author_by = models.ForeignKey(
        BlogAuthorModel,
        on_delete=models.CASCADE,
        related_name='blogs'
    )

    tags = models.ManyToManyField(
        BlogTagModel,
        related_name='posts'
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="draft"
    )

    def __str__(self):
        return self.title
