from django.contrib import admin
from blog.models import BlogAccountManagement
# Register your models here.


@admin.register(BlogAccountManagement)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('nid', 'account_name', 'account_number', 'account_email', 'account_url')
    list_display_links = ('nid', 'account_name')
    list_filter = ('account_name',)
    list_per_page = 50
