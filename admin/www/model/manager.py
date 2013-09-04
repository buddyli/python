#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from misc  import inject_db

@inject_db
def find_one(condition, **kwargs):
    '''查找用户'''
    return kwargs['mongo'].admin.find_one(condition)

@inject_db
def find(condition, size = 10, skip=0, **kwargs):
    '''查找列表'''
    data = kwargs['mongo'].admin.find(condition).sort('addtime', -1)
    if size:
        data.limit(size)
    if skip:
        data.skip(skip)
    return data

@inject_db
def save(manager, **kwargs):
    '''保存账号'''
    if 'addtime' not in manager:
        from datetime import datetime
        manager['addtime'] = datetime.now()
    return kwargs['mongo'].admin.save(manager)

@inject_db
def remove(condition, **kwargs):
    '''删除账号'''
    return kwargs['mongo'].admin.remove(condition)