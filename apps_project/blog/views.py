# Create your views here.
import json
import markdown
from django.http import HttpRequest,JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import MarkdownArticle
from .getbloginfo import get_blog_label_info


def base_home(request):
    """

    :param request:
    :return:
    """
    return render(request, "home.html")


def detail(request, pk):
    post = get_object_or_404(MarkdownArticle, pk=pk)
    # 记得在顶部引入 markdown 模块
    post.body = markdown.markdown(post.article_content,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'home.html', context={'post': post})


def get_label_info(request):
    """
    获取所有文章的标签和数量
    :param request:
    :return:
    """
    if request.method == "POST":
        info = []
        info = get_blog_label_info()
        print(info)
        return JsonResponse({'info': info})


def get_label_info1(request):
    """
    获取所有文章的标签和数量
    :param request:
    :return:
    """
    info_list = get_blog_label_info()
    for i in info_list:
        info = i
    print("11111111")
    print(info)
    return render(request, 'home.html', {'abc': info})