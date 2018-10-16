import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from blog.models import Post, Category, Tag


def create_tag(name):
    return Tag.objects.create(name=name)


def create_category(name):
    return Category.objects.create(name=name)


def create_post(title, description, published, content):
    category = create_category("Category1")
    return Post.objects.create(title=title, description=description, published=published,
                               content=content, posted_on=timezone.now(), category=category)


class BlogIndexViewTests(TestCase):
    def test_no_posts(self):
        """
        If no posts exist, 'posts' context variable should be an empty list
        """
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['posts'], [])

    def test_published_posts(self):
        """
        Index page shows only published posts
        """
        create_post("Test post", "Test description", True, "Test content")
        create_post("Test post1", "Test description1", False, "Test content1")
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['posts']), 1)
        self.assertQuerysetEqual(response.context['posts'], [
                                 '<Post: Test post>'])

    def test_categories_load_successfully(self):
        """
        Check if index page successfully load _sidebar.html
        with all categories
        """
        create_category("Category1")
        create_category("Category2")
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(len(response.context['categories']), 2)
        self.assertQuerysetEqual(response.context['categories'], ['<Category: Category1>', '<Category: Category2>'])
    
    def test_tags_load_successfully(self):
        """
        Check if index page successfully load _sidebar.html
        with all categories
        """
        create_tag("Tag1")
        create_tag("Tag2")
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(len(response.context["tags"]), 2)
        self.assertQuerysetEqual(response.context["tags"], ["<Tag: Tag1>", "<Tag: Tag2>"])


class BlogDetailViewTests(TestCase):
    def test_should_return_not_found(self):
        """
        404 Not Found page should be returned when the post is not found
        """
        response = self.client.get(reverse("blog:detail", kwargs={"slug": "random-post"}))
        self.assertEqual(response.status_code, 404)

    def test_should_show_correct_article(self):
        """
        Detail page should show correct post based on post's slug
        """
        post = create_post("Post1", "Post1 description", True, "Post1 Content")
        response = self.client.get(reverse("blog:detail", kwargs={"slug": post.url_slug}))
        self.assertEqual(response.context["post"], post)
        self.assertEqual(response.context["post"].url_slug, post.url_slug)
        self.assertEqual(response.context["post"].title, post.title)
