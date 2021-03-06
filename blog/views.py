import operator
from functools import reduce
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views import generic
from django.utils.translation import gettext as _
from blog.models import Category, Post, Tag


class IndexView(generic.ListView):
    """
    Show list of the latest published posts
    """
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = _("Latest posts")
        context["categories"] = get_categories()
        context["tags"] = get_tags()
        context["archive_dates"] = get_archive_dates()
        return context

    def get_queryset(self):
        result = super(IndexView, self).get_queryset()

        query = self.request.GET.get("q")
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_, (Q(title__icontains=q) for q in query_list)), published=True)
        else:
            result = result.filter(published=True)

        return result.order_by('-posted_on')


class CategoryView(generic.ListView):
    """
    Get a Category by url_slug and all published posts that belong to it
    """
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = get_categories()
        context["tags"] = get_tags()
        context["archive_dates"] = get_archive_dates()
        context["page_title"] = _("Posts by '%(category)s' category") % {
            'category': self.category.name}
        return context

    def get_queryset(self):
        self.category = get_object_or_404(
            Category, url_slug=self.kwargs['slug'])
        return self.category.post_set.filter(published=True).order_by("-posted_on")


class TagView(generic.ListView):
    """
    Get a tag by url_slug and all published posts that belong to it
    """
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = get_categories()
        context["tags"] = get_tags()
        context["archive_dates"] = get_archive_dates()
        context["page_title"] = _("Posts by '%(tag)s' tag") % {
            'tag': self.tag.name}
        return context

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, url_slug=self.kwargs['slug'])
        return self.tag.post_set.filter(published=True).order_by("-posted_on")


class DetailView(generic.DetailView):
    """
    Show a single post
    """
    template_name = "blog/detail.html"
    model = Post
    slug_field = "url_slug"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = get_categories()
        context["tags"] = get_tags()
        context["archive_dates"] = get_archive_dates()
        return context


class MonthArchiveView(generic.MonthArchiveView):
    """
    Get all published posts by year and month
    """
    template_name = "blog/index.html"
    model = Post
    date_field = "posted_on"
    context_object_name = "posts"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = get_categories()
        context["tags"] = get_tags()
        context["archive_dates"] = get_archive_dates()
        context["page_title"] = _("Posts by %(year)s year and %(month)s month") % {
            'year': self.kwargs["year"], 'month': self.kwargs["month"]}
        return context

    def get_queryset(self):
        return Post.objects.filter(published=True).order_by("-posted_on")


def get_categories():
    """
    Get all categories from DB
    """
    return Category.objects.all().order_by('name')


def get_tags():
    """
    Get all tag from DB
    """
    return Tag.objects.all().order_by('name')


def get_archive_dates():
    """
    Get Posts' dates
    """
    return Post.objects.filter(published=True).datetimes('posted_on', 'month', 'DESC')
