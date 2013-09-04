#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:test.py
import os
import fnmatch
import sys
import re

#异常捕获的用法
try:
	for f in os.listdir('/home/licb/documents/shells'):#遍历目录，并且添加对异常的捕获
		#返回文件所在的目录
		#print os.path.dirname(os.path.abspath(f))
		pass
except Exception, e:
	print 'error dir!please check: %s' % e
else:
	pass
finally:
	pass

#遍历指定的目录，获取符合条件的文件
#类的方法与普通模块的区别是：方法的第一个参数是‘self’
def _filter(dir,regex):
	_files = []
	for f in os.listdir(dir):
		if fnmatch.fnmatch(f,regex):
			_files.append(f)

	return _files

#测试一下_fileter是不是正确的
def test():
	_files = _filter('/home/licb/documents/shells','*.sh')
	for f in _files:
		print os.path.abspath(f)

from urllib import quote
from urllib import unquote
print quote('您的新密码是')
print unquote('''%E4%BA%B2%E7%88%B1%E7%9A%84%E7%94%A8%E6%88%B7%2C%E6%82%A8%E7%9A%84%E6%96%B0%E5%AF%86%E7%A0%81%E6%98%AF357212%2C%E8%AF%B7%E5%8F%8A%E6%97%B6%E7%99%BB%E5%BD%95%E4%BD%BF%E7%94%A8.%E4%B8%BA%E4%BF%9D%E6%8A%A4%E6%82%A8%E7%9A%84%E5%B8%90%E5%8F%B7%E5%AE%89%E5%85%A8%2C%E5%BB%BA%E8%AE%AE%E6%82%A8%E5%B0%BD%E5%BF%AB%E4%BF%AE%E6%94%B9%E5%AF%86%E7%A0%81.%E5%A6%82%E9%9D%9E%E6%9C%AC%E4%BA%BA%E6%93%8D%E4%BD%9C%E5%8F%AF%E4%B8%8D%E4%BA%88%E7%90%86%E4%BC%9A%2C%E8%AF%A6%E8%AF%A212580.''')
print sys.exc_info()
print sys.copyright

str = '''dfdfffdfdf{dfasdfasdfas$%#@$4}d}fsdfaf'''
m = re.search(r'\{(?P<guo>[^\}]*)\}',str)
if m:
	print m.group('guo')
