from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('likes',)
    search_fields = (
        'title',
    )
    list_display = (
        'title',
        'slug',
        'published_at',
        'author',
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('post', 'author',)
    search_fields = ('post', 'author',)
    list_display = ('post', 'text',)
