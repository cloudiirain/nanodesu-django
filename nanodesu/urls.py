from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'nanodesu.views.index', name='index'),
    url(r'^series/(?P<slug>[\w\-]+)/$', 'nanodesu.views.view_series', name='series-detail'),
    url(r'^chapter/(?P<slug>[\w\-]+)/$', 'nanodesu.views.view_post', name='post-detail'),
    url(r'^admin/', admin.site.urls),
]
