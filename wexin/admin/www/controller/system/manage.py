#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from bottle import route, mako_template as template, redirect, request, response
from setting import *
from misc  import *
from misc.hash import md5 #md5 方法

###### haeder funs
def auth_check(callback):
    '''验证用户是否登陆'''
    def wrapper(*args, **kargs):
        if 'account' in request.session and request.session['account'] is not None:
            return callback(*args, **kargs)
        else:
            redirect('/manage/login')     
    return wrapper

###### route
@route('/manage/login', method='GET')
def login_form():
    '''后台管理登陆页面'''
    account = request.get_cookie("manager") or ''
    remember = request.get_cookie("remember")
    return template('tpl/system/login', site_opt = site_opt, account= account, remeber=remember)

@route('/manage/login', method='POST')
def do_login():
    '''后台管理登陆逻辑'''
    account = request.forms.get('username')
    password = request.forms.get('password')

    remmeber_me(account)
    check_account(account, password)
    manager = find_manager({"account":account, "password":md5(password)})
    if not manager:
        redirect('/manage/login')

    set_session('account', account)
    redirect('/manage/dashboard')

@route('/manage/logout', method='GET')
def do_logout():
    '''退出登陆'''
    request.session['account'] = None
    request.session.save()
    redirect('/manage/dashboard')    

@route('/manage/dashboard', method='GET')
@auth_check
def dashboard():
    '''默认首页'''
    data = {
        'account': request.session['account'] or 'Hack',
    }
    return template('tpl/system/main', site_opt = site_opt, data = data)

@route('/manage/profile')
@auth_check
def profile():
    '''个人信息'''
    from datetime import date
    data = {
        'account': request.session['account'] or None,
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
        redirect('/manage/login')

def find_member(condition, **kwargs):
    '''查找普通用户'''
    from model.member import find_one as find_member
    return find_member(condition, **kwargs)

def find_manager(condition, **kwargs):
    '''查找管理员用户'''
    from model.manager import find_one as find_manager
    return find_manager(condition, **kwargs)

def save_manager(member, **kwargs):
    '''保存管理账号'''
    from model.manager import save as save_manager
    return save_manager(member, **kwargs)





    