# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.utils import simplejson

from lfs_managemanage.conf import settings

def get_config(request):
    json = simplejson.dumps(settings)
    return HttpResponse(json, mimetype='application/json')
