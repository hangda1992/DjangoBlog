# 获取blog相关信息
from .models import MarkdownArticle


class GetBlogInfo(object):

    def __init__(self):
        self.data = []
        blog_info_list = MarkdownArticle.objects.all().values()
        for blog_info in blog_info_list:
            self.data.append(
                {
                    'article_time_c': blog_info['article_time_c'],
                    'article_classification': blog_info['article_classification'],
                    'article_title': blog_info['article_time_c'],
                    'article_img': blog_info['article_img'],
                    'article_content': blog_info['article_content']
                }
            )

    def get_classification(self):
        """
        获取博客分类和数量
        :return:
        """
        classification_info = []
        classification_list = []
        for d_list in self.data:
            classification_list.append(d_list['article_classification'])
        classification_set = set(classification_list)
        for classification_i in classification_set:
            classification_info.append({
                classification_i: classification_list.count(classification_i)
            })
        return classification_info

    def get_article_msg(self):
        """
        获取文章所有信息
        :return:
        """
        return self.data
