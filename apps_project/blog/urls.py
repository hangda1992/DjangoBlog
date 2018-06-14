from django.conf.urls import url
from django.contrib import admin
from blog import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', views.base, name="home"),
    url(r'^home/(?P<pk>[0-9]+)/$', views.detail, name='detail'),

    ]
