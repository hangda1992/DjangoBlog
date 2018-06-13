from __future__ import unicode_literals
from django.db import models
from markdownx.models import MarkdownxField

# Create your models here.


class BlogAccountManagement(models.Model):
    """
    记录用户的基本信息：
    名字、
    分配的ID
    邮箱地址
    个人博客连接
    """
    nid = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=100, null=True)
    account_number = models.CharField(max_length=100, null=True)
    account_email = models.CharField(max_length=100, null=True)
    account_url = models.CharField(max_length=100, null=True)


class MarkdownArticle(models.Model):
    field = MarkdownxField()
    article_time_c = models.DateField(auto_now_add=True, null=True)
    article_time_u = models.DateField(auto_now=True, null=True)
    article_label = models.CharField(max_length=50, null=True)
    article_title = models.CharField(max_length=50, null=True)
    article_img = models.CharField(max_length=50, null=True)
