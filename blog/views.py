from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    latest_posts = Post.objects.filter(published=True).order_by("-posted_on")[:10]
    context = {
        "latest_posts": latest_posts,
    }
    return render(request, "blog/index.html", context)

def detail(request, post_slug):
    post = get_object_or_404(Post, url_slug=post_slug)
    return render(request, "blog/detail.html", {'post': post})