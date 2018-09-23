from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Main info", {"fields": [
            "title", "description", "content", "category"
        ]}),
        ("Publication info", {"fields": [
            "published", "posted_on"
        ]})
    ]
    list_display = ('title', 'url_slug', 'posted_on', 'published', 'category')
    list_filter = ['posted_on', 'published', 'category']
    search_fields = ['title']

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
