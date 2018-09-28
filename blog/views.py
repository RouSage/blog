from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic
from .models import Post, Category, Tag


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
        return context


def archive_date(request, year, month):
    """
    Get all published posts by year and month
    """
    posts = get_list_or_404(Post.objects.oder_by("-posted_on"), published=True,
                            posted_on__year=year, posted_on__month=month)[:10]
    context = {
        "posts": posts,
        "page_title": "Posts by {} year and {}th month".format(year, month),
        "categories": get_categories(),
        "tags": get_tags()
    }
    return render(request, "blog/index.html", context)


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
