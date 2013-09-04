#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import os
import sys
import fnmatch
import re

reload(sys)
sys.setdefaultencoding('utf-8')

def getFiles():
	dir = ['/data/log_bk/wap/23/','/data/log_bk/wap/24/','/data/log_bk/wap/124/','/data/log_bk/wap/125/']
	for path in dir:
		for f in os.listdir(path):
			fullPath = path+f
			print '正在处理%s...' % fullPath
			cmd = 'grep register %s|grep GET >>reg.log' % fullPath
			os.system(cmd)

	print 'fuck gx over....'


getFiles()