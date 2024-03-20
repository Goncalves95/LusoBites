from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content', 'ingredients_content',]
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'ingredients_content', 'method_content')
    

# Register your models here.
# This will allow you to create, update and delete blog posts from the admin panel.
admin.site.register(Comment)