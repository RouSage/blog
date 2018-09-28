from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Post, Category, Tag


def index(request):
    posts = get_list_or_404(Post.objects.order_by(
        "-posted_on"), published=True)[:10]
    context = {
        "posts": posts,
        "page_title": "Latest posts",
        "categories": get_categories(),
        "tags": get_tags()
    }
    return render(request, "blog/index.html", context)


def archive_date(request, year, month):
    posts = get_list_or_404(Post.objects.oder_by("-posted_on"), published=True,
                            posted_on__year=year, posted_on__month=month)[:10]
    context = {
        "posts": posts,
        "page_title": "Posts by {} year and {}th month".format(year, month)
    }
    return render(request, "blog/index.html", context)


def category(request, category_slug):
    category_by_slug = get_object_or_404(Category, url_slug=category_slug)
    context = {
        "posts": category_by_slug.post_set.filter(published=True).order_by("-posted_on"),
        "page_title": "Posts by '{}' category".format(category_by_slug.name),
        "categories": get_categories(),
        "tags": get_tags()
    }
    return render(request, "blog/index.html", context)


def tag(request, tag_slug):
    tag_by_slug = get_object_or_404(Tag, url_slug=tag_slug)
    context = {
        "posts": tag_by_slug.post_set.filter(published=True).order_by("-posted_on"),
        "page_title": "Posts by '{}' tag".format(tag_by_slug.name),
        "categories": get_categories(),
        "tags": get_tags()
    }
    return render(request, "blog/index.html", context)


def detail(request, post_slug):
    post = get_object_or_404(Post, url_slug=post_slug)
    context = {
        "post": post,
        "categories": get_categories(),
        "tags": get_tags()
    }
    return render(request, "blog/detail.html", context)


def get_categories():
    return Category.objects.all().order_by('name')


def get_tags():
    return Tag.objects.all().order_by('name')
