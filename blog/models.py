from django.db import models
from tinymce import models as tinymce_models
from django.utils import timezone
from django.utils.translation import pgettext_lazy, gettext_lazy as _
from .utils import get_unique_slug


class Category(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name=_('name'))
    url_slug = models.SlugField(
        unique=True,
        db_index=True,
        max_length=50)
    created_at = models.DateTimeField(
        verbose_name=pgettext_lazy("category", "Created at"),
        default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.url_slug:
            self.url_slug = get_unique_slug(self, 'name', 'url_slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Tag(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name=_('name'))
    url_slug = models.SlugField(
        unique=True,
        db_index=True,
        max_length=50)
    created_at = models.DateField(
        verbose_name=pgettext_lazy("tag", "Created at"),
        default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.url_slug:
            self.url_slug = get_unique_slug(self, 'name', 'url_slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class Post(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name=_('title'))
    description = models.TextField(
        max_length=5000,
        verbose_name=_('description'))
    content = tinymce_models.HTMLField(
        verbose_name=_('content')
    )
    url_slug = models.SlugField(
        unique=True,
        db_index=True,
        max_length=50)
    published = models.BooleanField(
        default=False,
        verbose_name=_('published'))
    posted_on = models.DateTimeField(
        db_index=True,
        verbose_name=_('posted_on'))
    # Category FK
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name=_('category'))
    # Tag Many-to-many
    tags = models.ManyToManyField(
        Tag,
        verbose_name=_('tags'))

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.url_slug:
            self.url_slug = get_unique_slug(self, 'title', 'url_slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
