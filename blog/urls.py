from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    # ex: /blog/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /blog/lorem_ipsum
    path("<slug:slug>/", views.DetailView.as_view(), name="detail"),
    # ex: /blog/archive/2018/10
    path("archive/<int:year>/<int:month>/",
        views.MonthArchiveView.as_view(month_format="%m"), name="archive"),
    # ex: /blog/archive/programming
    path("categories/<slug:slug>/", views.CategoryView.as_view(), name="category"),
    # ex: /blog/archive/web
    path("tags/<slug:slug>/", views.TagView.as_view(), name="tag")
]
