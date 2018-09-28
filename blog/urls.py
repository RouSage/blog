from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    # ex: /blog/
    path("", views.index, name="index"),
    # ex: /blog/lorem_ipsum
    path("<slug:post_slug>/", views.detail, name="detail"),
    # ex: /blog/archive/2018/10
    path("archive/<int:year>/<int:month>/", views.archive_date, name="archive_date"),
    # ex: /blog/archive/programming
    path("categories/<slug:category_slug>/", views.category, name="category"),
    # ex: /blog/archive/web
    path("tags/<slug:tag_slug>/", views.tag, name="tag")
]
