# Create your views here.
import json
import markdown
from django.http import HttpRequest,JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import MarkdownArticle
from .getbloginfo import GetBlogInfo


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
                                     'markdown.extensions.tables'
                                  ])
    return render(request, 'home.html', context={'post': post})


def get_article_info(request):
    """
    获取所有文章的信息
    :param request:
    :return:
    """
    info = {
        'status': 400,
        'data': ['']
    }
    if request.method == "GET":
        try:
            blog = GetBlogInfo()
            info['data'] = blog.get_article_msg()
            for blog_info in info['data']:

                a = blog_info['article_content']
                a = ''.join(a)
                a = markdown.markdown(a,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])

                blog_info['article_content'] = a
            info['status'] = 200
        except Exception as e:
            print(e)

    return JsonResponse(info)


def get_label_info(request):
    """
    获取博客文章分类
    :param request:
    :return:
    """
    info = {
        'status': 400,
        'data': []
    }
    if request.method == 'GET':
        try:
            blog = GetBlogInfo()
            info['data'] = blog.get_classification()
            info['status'] = 200
        except Exception as e:
            print(e)

    return JsonResponse(info)