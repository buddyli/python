#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import sys
import os

dirname = os.path.dirname(os.path.abspath(__file__))

sys.path.append(dirname)
sys.path.append(os.path.dirname(dirname))

from misc.mongo import mongo as m
from misc.hash import md5

@m.save(name="admin")
def save_admin(*args, **kwargs):pass


def create_admin():
	from model.admin import admin_field
	admin = {}
	admin['account'] = 'admin'
	admin['password'] = md5('admin')
	print admin
	save_admin(admin)


if __name__ == '__main__':
	create_admin()