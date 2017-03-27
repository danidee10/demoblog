from django.db import models
from django.contrib.auth.models import User


class Common(models.Model):
    """Common fields shared by models."""

    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    """Categories for blog posts."""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PublishedManager(models.Manager):
    """A custom manager that only shows published posts."""

    def get_queryset(self):
        """show only published posts."""
        return super().get_queryset().filter(published=True).order_by('-create_date')


class Post(Common):
    """Blog post model."""

    author = models.ForeignKey(User, editable=False, null=True)
    categories = models.ManyToManyField(Category, blank=True)

    title = models.CharField(max_length=200, unique=True)
    excerpt = models.TextField(
        max_length=500, unique=True, null=True, blank=True
        )
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField(max_length=10000, unique=True)

    # image should be made unique by overriding save() method of the model
    image = models.ImageField(upload_to='articles')
    published = models.BooleanField(default=False)

    # Managers
    objects = models.Manager()
    published_posts = PublishedManager()

    def __str__(self):
        return self.title

class Comment(Common):
    """Comments on blog posts"""
    user = models.ForeignKey(User, null=True)
    comment = models.TextField(max_length=5000, unique=True)
    post = models.ForeignKey(Post, related_name='comments')

    def __str__(self):
        return self.post.title
