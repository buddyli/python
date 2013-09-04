#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from bottle import route, mako_template as template, redirect, request, response, Bottle
from setting import *
from misc.mongo  import mongo as m
from misc.hash import md5 #md5
from dashboard import auth_check

@route('/system/manager/add', method='GET')
@auth_check
def member_add():
    '''添加用户表单'''
    data = {
        'account': request.session['account'] or 'Hack',
    }
    return template('tpl/system/manager/add', site_opt = site_opt, data = data)

@route('/system/manager/add', method='POST')
@auth_check
def do_add():
    '''保存用户信息'''
    if request.forms.get('_id'):
        _id = "%s" % request.forms.get('_id')
        member = find_one({'_id':_id}) or {}
    member = {}
    from model.admin import admin_field as fields
    for p in fields:
        if p in request.forms and p !='password':
            member[p] = request.forms.get(p)
    #hash password
    if request.forms.get('password'):
        member['password'] = md5(request.forms.get('password'))

    save(member)
    redirect('/system/manager/list')

@route('/system/manager/delete', method='GET')
@auth_check
def delete():
    '''删除用户'''
    if request.query.get('_id'):
        remove({'_id': request.query._id})
    redirect('/system/manager/list?_uniq=%s' % request.query._uniq)


@route('/system/manager/edit', method='GET')
@auth_check
def edit():
    '''编辑用户'''
    data = {
        'account': request.session['account'] or 'Hack',
        'item' : find_one({'_id': request.query.get('_id')}) if request.query.get('_id') else None
    }

    return template('tpl/system/manager/edit', site_opt = site_opt, data = data)

@route('/system/manager/list', method='GET')
@auth_check
def list():
    '''用户列表'''
    #_uniq = request.query._uniq
    page = request.query.page or 1
    page = int(page) if int(page) > 0 else 1
    size = 15
    skip = (page - 1) * size
    cursor = find_all({}, size, skip)
    data = {
        'account': request.session['account'] or 'Hack',
        'members' : cursor,
        'pagenation' : pagenation(cursor.count(), page, size),
        'cur_page' : page
    }
    return template('tpl/system/manager/list', site_opt = site_opt, data = data)

########### private funs
def pagenation(total, page, size):
    '''生成分页是数据'''
    from misc.pagenation import create_pagenation
    return create_pagenation(total, page, size)

@m.find(name="admin")
def find_all(condition, size = 10, skip=0, **kwargs):pass

@m.find_one(name="admin")
def find_one(condition, **kwargs):pass

@m.save(name="admin")
def save(condition, **kwargs):pass

@m.remove(name="admin")
def remove(member, **kwargs):pass

    