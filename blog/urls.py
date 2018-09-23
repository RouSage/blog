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
    # ex: /blog/programming
    path("archive/<slug:category_slug>/", views.archive_category, name="archive_category")
]
