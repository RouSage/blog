from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)
    url_slug = models.CharField(max_length=250)
    created_at = models.DateTimeField(verbose_name="created at")

class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=5000)
    content = models.TextField()
    url_slug = models.CharField(max_length=250)
    published = models.BooleanField(default=False)
    posted_on = models.DateTimeField()
    # Category FK
    category = models.ForeignKey(Category, on_delete=models.CASCADE)