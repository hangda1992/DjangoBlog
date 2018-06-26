# 获取blog相关信息
from .models import MarkdownArticle


def get_blog_label_info():
    """
    获取博客主题和对应的主题数量
    :return:
    """
    info = []
    blog_info_list = []
    blog_infos = MarkdownArticle.objects.all().values()
    for blog_info in blog_infos:
        blog_info_list.append(blog_info['article_label'])
    blog_info_set = set(blog_info_list)
    for set_i in blog_info_set:
        info.append({
            set_i: blog_info_list.count(set_i)
            }
        )
    return info
