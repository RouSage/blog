from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.filter(published=True).order_by("-posted_on")[:10]
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

def archive(request, year, month):
    posts = Post.objects.filter(posted_on__year=year, posted_on__month=month)
    context = {
        "posts": posts
    }
    return render(request, "blog/index.html", context)


def detail(request, post_slug):
    post = get_object_or_404(Post, url_slug=post_slug)
    return render(request, "blog/detail.html", {'post': post})
