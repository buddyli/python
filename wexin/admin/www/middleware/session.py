#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import bottle
from bottle import request, route, hook
import beaker.middleware
from setting import session_path

session_opts = {
    'session.type': 'file',
    'session.data_dir': session_path,
    'session.auto': True,
}

app_middlware = beaker.middleware.SessionMiddleware(bottle.app(), session_opts)
#app_session = app.request.environ.get('beaker.session')

@hook('before_request')
def setup_request():
    request.session = request.environ['beaker.session']