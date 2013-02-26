
from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns('',

    url(r'^manage/manage/$', 'lfs_managemanage.views.get_config', name='get_config'),
)
