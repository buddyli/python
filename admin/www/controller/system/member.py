#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from bottle import route, mako_template as template, redirect, request, response, Bottle
from setting import *
from misc  import inject_db
from utils.hash import md5 #md5
from manage import auth_check
import math

@route('/manage/member/add', method='GET')
@auth_check
def member_add():
    '''添加用户表单'''
    data = {
        'account': request.session['account'] or 'Hack',
    }
    return template('tpl/system/member/add', site_opt = site_opt, data = data)

@route('/manage/member/add', method='POST')
@auth_check
def do_add():
    '''保存用户信息'''
    from model import member_props
    member = find_member({'passport':request.forms.get('passport')}) or {}
    for prop in member_props:
        if prop in request.forms:
            member[prop] = request.forms.get(prop)
    #hash password
    passwd_str = request.forms.get('password') if request.forms.get('password') else request.forms.get('passport')[-6:]
    member['password'] = md5(passwd_str)
    save_member(member)
    redirect('/manage/member/list')

@route('/manage/member/delete', method='GET')
@auth_check
def delete():
    '''删除用户'''
    _id = request.query._id
    _uniq = request.query._uniq
    if _id:
        from bson.objectid import ObjectId
        delete_member({'_id': ObjectId(_id)})
    redirect('/manage/member/list?_uniq=%s' % _uniq)


@route('/manage/member/edit', method='GET')
@auth_check
def edit():
    '''编辑用户'''
    data = {
        'account': request.session['account'] or 'Hack',
    }
    _id = request.query._id
    if _id:
        from bson.objectid import ObjectId
        data['member'] = find_member({'_id': ObjectId(_id)})

    return template('tpl/system/member/edit', site_opt = site_opt, data = data)

@route('/manage/member/list', method='GET')
@auth_check
def list():
    '''用户列表'''
    #_uniq = request.query._uniq
    page = request.query.page or 1
    page = int(page) if int(page) > 0 else 1
    size = 15

    data = {
        'account': request.session['account'] or 'Hack',
    }

    skip = (page - 1) * size
    data['members'] = find_list({}, size, skip)

    # if data['members']:
    #     last = data['members'].count(True) - 1
    #     data['_uniq'] = data['members'][last]['_id']

    data['pagenation'] = pagenation(data['members'].count(), page, size)
    data['cur_page'] = page

    return template('tpl/system/member/list', site_opt = site_opt, data = data)

########### private funs
def pagenation(total, page, size):
    '''生成分页是数据'''
    from misc.pagenation import create_pagenation
    return create_pagenation(total, page, size)

def delete_member(condition, **kwargs):
    from model.member import remove as delete_member
    return delete_member(condition, **kwargs)

def find_list(condition, size = 10, skip=0, **kwargs):
    '''查找用户列表'''
    from model.member import find as find_all
    return find_all(condition, **kwargs)

def find_member(condition, **kwargs):
    '''查找一个用户'''
    from model.member import find_one as find_member
    return find_member(condition, **kwargs)

def save_member(member, **kwargs):
    '''保存用户信息'''
    from model.member import save as save_member
    return save_member(member, **kwargs)

    