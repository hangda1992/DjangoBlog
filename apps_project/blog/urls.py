from django.conf.urls import url
from django.contrib import admin
from blog import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', views.base_home, name="base_home"),
    url(r'^home/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^home/get_article_info$', views.get_article_info, name='get_article_info'),
    url(r'^home/get_label_info$', views.get_label_info, name='get_label_info'),

    ]
