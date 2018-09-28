from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Post, Category, Tag
from django.db.models import Count


def index(request):
    posts = get_list_or_404(Post.objects.order_by(
        "-posted_on"), published=True)[:10]
    categories = Category.objects.annotate(
        n_posts=Count('post')).order_by('name')
    tags = Tag.objects.all().order_by('name')
    context = {
        "posts": posts,
        "page_title": "Latest posts",
        "categories": categories,
        "tags": tags
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
    category = get_object_or_404(Category, url_slug=category_slug)
    context = {
        "posts": category.post_set.all(),
        "page_title": "Posts by '{}' category".format(category.name)
    }
    return render(request, "blog/index.html", context)


def tag(request, tag_slug):
    tag = get_object_or_404(Tag, url_slug=tag_slug)
    context = {
        "posts": tag.post_set.all(),
        "page_tile": "Posts by '{}' tag".format(tag.name)
    }
    return render(request, "blog/index.html", context)


def detail(request, post_slug):
    post = get_object_or_404(Post, url_slug=post_slug)
    context = {
        "post": post
    }
    return render(request, "blog/detail.html", context)
