from django.db import models
from django.utils import timezone
from .utils import get_unique_slug


class Category(models.Model):
    name = models.CharField(max_length=250)
    url_slug = models.SlugField(unique=True, db_index=True, max_length=50)
    created_at = models.DateTimeField(
        verbose_name="created at", default=timezone.now())

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.url_slug:
            self.url_slug = get_unique_slug(self, 'name', 'url_slug')
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=150)
    url_slug = models.SlugField(unique=True, db_index=True, max_length=50)
    created_at = models.DateField(
        verbose_name="created ad", default=timezone.now())

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.url_slug:
            self.url_slug = get_unique_slug(self, 'name', 'url_slug')
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=5000)
    content = models.TextField()
    url_slug = models.SlugField(unique=True, db_index=True, max_length=50)
    published = models.BooleanField(default=False)
    posted_on = models.DateTimeField(db_index=True)
    # Category FK
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Tag Many-to-many
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.url_slug:
            self.url_slug = get_unique_slug(self, 'title', 'url_slug')
        super().save(*args, **kwargs)
