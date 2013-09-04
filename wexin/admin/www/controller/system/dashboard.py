#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from bottle import route, mako_template as template, redirect, request, response
from setting import *
from misc.mongo  import mongo as m
from misc.hash import md5 #md5 方法

###### haeder funs
def auth_check(callback):
    '''验证用户是否登陆'''
    def wrapper(*args, **kargs):
        if 'account' in request.session and request.session['account'] is not None:
            return callback(*args, **kargs)
        else:
            redirect('/system/login')     
    return wrapper

###### route
@route('/system/login', method='GET')
def login_form():
    '''后台管理登陆页面'''
    account = request.get_cookie("manager") or ''
    remember = request.get_cookie("remember")
    return template('tpl/system/login', site_opt = site_opt, account= account, remeber=remember)

@route('/system/login', method='POST')
def do_login():
    '''后台管理登陆逻辑'''
    account = request.forms.get('username')
    password = request.forms.get('password')

    remmeber_me(account)
    check_account(account, password)
    manager = find_manager({"account":account, "password":md5(password)})
    if not manager:
        redirect('/system/login')

    set_session('account', account)
    redirect('/system/dashboard')

@route('/system/logout', method='GET')
def do_logout():
    '''退出登陆'''
    request.session['account'] = None
    request.session.save()
    redirect('/system/dashboard')    

@route('/system/dashboard', method='GET')
@route('/', method = 'GET')
@auth_check
def dashboard():
    '''默认首页'''
    data = {
        'account': request.session['account'] or 'Hack',
    }
    return template('tpl/system/main', site_opt = site_opt, data = data)

@route('/system/profile')
@auth_check
def profile():
    '''个人信息'''
    from datetime import date
    data = {
        'account': request.session['account'] or None,
        'user' : find_manager({'account':request.session['account']}),
        'today' : date.today()
    }
    return template('tpl/system/profile', site_opt = site_opt, data = data)


########## priv funs

def remmeber_me(account):
    '''记住账号'''
    remember = request.forms.get('remember')
    if remember:
        response.set_cookie("manager", account, path = '/manage')
        response.set_cookie("remember", remember)
    else:
        response.delete_cookie("manager")
        response.delete_cookie("remember")

def set_session(name, value):
    '''设置session'''
    request.session[name] = value
    request.session.save()

def check_account(account, password):
    '''校验用户名密码'''
    if not account or not password:
        redirect('/system/login')
@m.find_one('admin')
def find_manager(condition, **kwargs): pass





    