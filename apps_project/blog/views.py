from django.http import HttpResponse
from django.utils.safestring import mark_safe
import markdown
from django.shortcuts import render, get_object_or_404
from .models import Tt
from .models import MarkdownArticle
# Create your views here.


def base(request):
    return render(request, "home.html")


def detail(request, pk):
    post = get_object_or_404(MarkdownArticle, pk=pk)
    # 记得在顶部引入 markdown 模块
    post.body = markdown.markdown(post.field,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'home.html', context={'post': post})