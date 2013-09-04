#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from bottle import route, mako_template as template, redirect, request, response, Bottle
from setting import *
from misc.mongo  import mongo as m
from misc.hash import md5 #md5
from dashboard import auth_check

_name = 'uri'

@route('/system/%s/add' % _name, method='GET')
@auth_check
def show_add_form():
    '''添加数据表单'''
    data = {
        'account': request.session['account'] or 'Hack',
    }
    return template('tpl/system/%s/add' % _name, site_opt = site_opt, data = data)

@route('/system/%s/edit' % _name, method='GET')
@auth_check
def show_edit_form():
    '''编辑数据'''
    data = {
        'account': request.session['account'] or 'Hack',
        'item' : find_one({'_id': request.query.get('_id')}) if request.query.get('_id') else None
    }

    return template('tpl/system/%s/edit' % _name, site_opt = site_opt, data = data)

@route('/system/%s/list' % _name, method='GET')
@auth_check
def list():
    '''数据列表'''
    #_uniq = request.query._uniq
    page = request.query.page or 1
    page = int(page) if int(page) > 0 else 1
    size = 15
    skip = (page - 1) * size
    cursor = find_all({}, size, skip)
    data = {
        'account': request.session['account'] or 'Hack',
        'items' : cursor,
        'pagenation' : pagenation(cursor.count(), page, size),
        'cur_page' : page
    }
    return template('tpl/system/%s/list' % _name, site_opt = site_opt, data = data)

@route('/system/%s/add' % _name, method='POST')
@auth_check
def do_add():
    '''保存信息'''
    if request.forms.get('_id'):
        _id = "%s" % request.forms.get('_id')
        data = find_one({'_id':_id}) or {}
    else: data = {}
    from model.uri import uri_field as fields
    for p in fields:
        if p in request.forms:
            data[p] = request.forms.get(p)
    save(data)
    redirect('/system/%s/list' % _name)

@route('/system/%s/delete' % _name, method='GET')
@auth_check
def delete():
    '''删除数据'''
    if request.query._id:
        _id = request.query._id
        remove({'_id':_id})
    redirect('/system/%s/list?_page=%s' % (_name, request.query._page))

@route('/system/%s/refresh' % _name, method='GET')
@auth_check
def do_refresh():
    '''加载URL'''
    data = {
        'account': request.session['account'] or 'Hack',
        'items' : []
    }
    if request.query._id:
        _id = request.query._id
        entity = find_one({'_id':_id})
        if entity and 'url' in entity:
            from misc.http import RequestPool
            urls = entity['url'].split(',')
            rp = RequestPool(urls)
            data['items'] = rp.send()

    return template('tpl/system/%s/result' % _name, site_opt = site_opt, data = data)




########### private funs
def pagenation(total, page, size):
    '''生成分页是数据'''
    from misc.pagenation import create_pagenation
    return create_pagenation(total, page, size)

@m.find(name="%s" % _name)
def find_all(condition, size = 10, skip=0, **kwargs):pass

@m.find_one(name="%s" % _name)
def find_one(condition, **kwargs):pass

@m.save(name="%s" % _name)
def save(condition, **kwargs):pass

@m.remove(name="%s" % _name)
def remove(member, **kwargs):pass

    