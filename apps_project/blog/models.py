from __future__ import unicode_literals
from django.db import models
from mdeditor.fields import MDTextField
# Create your models here.


class BlogAccountManagement(models.Model):
    """
    记录用户的基本信息：
    名字
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
    """
    markdown文件存入改数据库
    article_time_c 创建时间
    article_time_u 修改时间
    article_classification 文章分类
    article_title 文章标题
    article_img 文章展示图片路径和名称
    article_content 文章内容
    """
    article_time_c = models.DateField(auto_now_add=True, null=True)
    article_time_u = models.DateField(auto_now=True, null=True)
    # article_label = models.CharField(max_length=50, null=True)
    article_classification = models.CharField(max_length=50, null=True)
    article_title = models.CharField(max_length=50, null=True)
    article_img = models.CharField(max_length=50, null=True)
    article_content = MDTextField(null=True)
