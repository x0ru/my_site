from django.contrib import admin
from .models import Post, Author, Tag


class AdminPost(admin.ModelAdmin):
    list_filter = ('author', 'date', 'tags')
    list_display = ('title', 'date', 'author')
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Author)
admin.site.register(Post, AdminPost)
admin.site.register(Tag)

