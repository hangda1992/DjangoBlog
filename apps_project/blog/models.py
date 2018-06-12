from __future__ import unicode_literals
from django.db import models
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


class Article(models.Model):
    """
    文章创建时间 article_time_c
    文章更新时间 article_time_u
    文章标签 article_label
    文章标题 article_title
    文章图片 article_img
    文章内容 article_content
    """
    id = models.AutoField(primary_key=True)
    article_time_c = models.DateField(auto_now_add=True)
    article_time_u = models.DateField(auto_now=True)
    article_label = models.CharField(max_length=50)
    article_title = models.CharField(max_length=50)
    article_img = models.CharField(max_length=50)
    article_content = models.TextField(null=True)
