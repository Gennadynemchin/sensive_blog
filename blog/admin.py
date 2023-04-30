from django.contrib import admin
from blog.models import Post, Tag, Comment

'''
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
'''
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('likes',)
    search_fields = (
        'title',
        'author',
    )
    # readonly_fields = ("created_at",)
    list_display = (
        'title',
        'slug',
        'published_at',
        'author',
    )
    # list_editable = ("new_building",)
    # list_filter = ("new_building",)
    # inlines = [FlatInline,]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('post', 'author')
    search_fields = ('post', 'author', 'published_at',)
    list_display = ('post', 'author', 'published_at', 'text')
