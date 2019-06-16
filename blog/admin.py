from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (_("Main info"), {"fields": [
            "title", "description", "content", "category", "tags"
        ]}),
        (_("Publication info"), {"fields": [
            "published", "posted_on"
        ]})
    ]
    list_display = ('title', 'url_slug', 'posted_on',
                    'published', 'category', 'get_tags')
    list_filter = ['title', 'posted_on', 'published', 'category']
    search_fields = ['title', 'category']

    def get_tags(self, obj):
        return ", ".join([t.name for t in obj.tags.all()])


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
