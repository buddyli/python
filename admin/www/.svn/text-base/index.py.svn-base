#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from bottle import route,default_app, template, run
from controller import * #导入所有的控制器
from middleware.session import *
from setting import site_opt

##首页
@route('/', method='GET')
def default():
    redirect('/system/dashboard')

if __name__ == '__main__':
    run(host='localhost', port=8000, debug=True,reloader=True, app = app_middlware)
else:
    application = app_middlware