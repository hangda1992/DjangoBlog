from .models import MarkdownArticle
from django.db import models
from django.contrib import admin
from blog.models import BlogAccountManagement
from markdownx.widgets import AdminMarkdownxWidget
# Register your models here.


@admin.register(BlogAccountManagement)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('nid', 'account_name', 'account_number', 'account_email', 'account_url')
    list_display_links = ('nid', 'account_name')
    list_filter = ('account_name',)
    list_per_page = 50


# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('article_time_c', 'article_time_u', 'article_label', 'article_title', 'article_img',
#                     'article_content')

@admin.register(MarkdownArticle)
class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }

