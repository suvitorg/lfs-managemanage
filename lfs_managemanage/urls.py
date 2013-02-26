
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings


urlpatterns = patterns('lfs_managemanage.views',
    url(r'^manage/manage/$', 'get_config', name='get_config'),
)
