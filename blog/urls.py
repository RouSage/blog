from django.urls import path
from . import views
from blog.feeds import LatestPostsFeed


app_name = "blog"
urlpatterns = [
    # ex: /
    path("", views.IndexView.as_view(), name="index"),
    # ex: /lorem_ipsum
    path("<slug:slug>/", views.DetailView.as_view(), name="detail"),
    # ex: /archive/2018/10
    path("archive/<int:year>/<int:month>/",
         views.MonthArchiveView.as_view(month_format="%m"), name="archive"),
    # ex: /categories/programming
    path("categories/<slug:slug>/", views.CategoryView.as_view(), name="category"),
    # ex: /tags/web
    path("tags/<slug:slug>/", views.TagView.as_view(), name="tag"),
    # ex: /feed/
    path("latest/feed/", LatestPostsFeed(), name="feed"),
]
