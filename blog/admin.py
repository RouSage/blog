from django.contrib import admin
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Main info", {"fields": [
            "title", "description", "content", "category", "tags"
        ]}),
        ("Publication info", {"fields": [
            "published", "posted_on"
        ]})
    ]
    list_display = ('title', 'url_slug', 'posted_on', 'published', 'category')
    list_filter = ['posted_on', 'published', 'category', 'tags']
    search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": [
            "name", "created_at"
        ]})
    ]
    list_display = ('name', 'url_slug', 'created_at')
    list_filter = ['created_at']
    search_fields = ['name']

class TagAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": [
            "name", "created_at"
        ]})
    ]
    list_display = ('name', 'url_slug', 'created_at')
    list_filter = ['created_at']
    search_fields = ['name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
