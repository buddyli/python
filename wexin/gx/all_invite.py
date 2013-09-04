#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:all_invite.py

import os
import sys
import fnmatch
import re

reload(sys)
sys.setdefaultencoding('utf-8')

"""
没有注册就没有IP地址和串号

客户端来源的别忘了加上。
"""
def getFiles():
	dir = '/data/logs/hjb/'
	flist = []
	regex = 'umserver.log.20130[4|5|6]*.bz2'
	for f in os.listdir(dir):
		if fnmatch.fnmatch(f,regex):
			#print f
			flist.append(f)

	for f in flist:
		print '正在处理%s...' % f
		fpath = dir + f
		cmd = '''bzcat %s|grep invatation|grep -v -e '2013-04-0[123456789]' >>gxinvite.log''' % fpath
		os.system(cmd)

	print 'fuck gx over....'

getFiles()