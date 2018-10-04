from django.shortcuts import get_object_or_404, get_list_or_404
from django.views import generic
from blog.models import Post, Category, Tag


class IndexView(generic.ListView):
    """
    Show list of the latest published posts
    """
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Latest posts"
        context["categories"] = get_categories()
        context["tags"] = get_tags()
        context["archive_dates"] = get_arhive_dates()
        return context

    def get_queryset(self):
        return get_list_or_404(Post.objects.order_by("-posted_on"),
                               published=True)[:10]


class CategoryView(generic.ListView):
    """
    Get a Category by url_slug and all published posts that belong to it
    """
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = get_categories()
        context["tags"] = get_tags()
        context["archive_dates"] = get_arhive_dates()
        context["page_title"] = "Posts by '{}' category".format(
            self.category.name)
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = get_categories()
        context["tags"] = get_tags()
        context["archive_dates"] = get_arhive_dates()
        context["page_title"] = "Posts by '{}' tag".format(self.tag.name)
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
        context["archive_dates"] = get_arhive_dates()
        return context


class MonthArchiveView(generic.MonthArchiveView):
    """
    Get all published posts by year and month
    """
    template_name = "blog/index.html"
    model = Post
    date_field = "posted_on"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = get_categories()
        context["tags"] = get_tags()
        context["archive_dates"] = get_arhive_dates()
        context["page_title"] = "Posts by {} year and {}nt month".format(
            self.kwargs["year"], self.kwargs["month"])
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


def get_arhive_dates():
    """
    Get Posts' dates
    """
    return Post.objects.filter(published=True).datetimes('posted_on', 'month', 'DESC')

