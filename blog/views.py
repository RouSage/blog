from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Post


def index(request):
    posts = get_list_or_404(Post.objects.order_by("-posted_on"), published=True)[:10]
    context = {
        "posts": posts,
        "page_title": "Latest posts"
    }
    return render(request, "blog/index.html", context)

def archive(request, year, month):
    posts = get_list_or_404(Post.objects.oder_by("-posted_on"), published=True,
                            posted_on__year=year, posted_on__month=month)[:10]
    context = {
        "posts": posts,
        "page_title": "Posts by {} year and {}th month".format(year, month)
    }
    return render(request, "blog/index.html", context)


def detail(request, post_slug):
    post = get_object_or_404(Post, url_slug=post_slug)
    context = {
        "post": post
    }
    return render(request, "blog/detail.html", context)
