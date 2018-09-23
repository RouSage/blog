import datetime
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=250)
    url_slug = models.SlugField(unique=True, db_index=True, max_length=50)
    created_at = models.DateTimeField(
        verbose_name="created at", default=timezone.now())

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=5000)
    content = models.TextField()
    url_slug = models.SlugField(unique=True, db_index=True, max_length=50)
    published = models.BooleanField(default=False)
    posted_on = models.DateTimeField(db_index=True)
    # Category FK
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
