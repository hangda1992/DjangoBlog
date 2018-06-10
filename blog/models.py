from __future__ import unicode_literals
from django.db import models

# Create your models here.


class BlogAccountManagement(models.Model):
    # db_table = 'blogAccountManagement'
    nid = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=100, null=True)
    account_number = models.CharField(max_length=100, null=True)
    account_email = models.CharField(max_length=100, null=True)
    account_url = models.CharField(max_length=100, null=True)


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    article_time = models