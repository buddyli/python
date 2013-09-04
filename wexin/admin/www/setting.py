#!/usr/bin/env python
# -*- encoding:utf-8 -*-

##站点的配置
site_opt = {
    'site_url': '',
    'static_url' : 'http://localhost/'  #必须以 / 结尾
}

##安全码
secret_key = "%￥#@ujygfU"

db_conf = {
    'uri' : '127.0.0.1:27017',   ##数据库地址
    'dbname' : 'umessage',  ##数据库名称
}

cache_path = "./cache/"  #缓存目录 必须以 / 结尾

session_path = "./session/" #session目录 必须以 / 结尾

