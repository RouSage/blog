from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post


class LatestPostsFeed(Feed):
    title = "RouSage Blog Latest Posts"
    link = "/latest/feed/"

    def items(self):
        return Post.objects.filter(published=True).order_by("-posted_on")[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse('blog:detail', args=[item.url_slug])
