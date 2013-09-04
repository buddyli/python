#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:gxreset.py

import os
import sys
import fnmatch
import re

reload(sys)
sys.setdefaultencoding('utf-8')

"""
捞取广西6月重置密码的数据
"""
def getFiles():
	dir = '/data/logs/log_hjb/'
	flist = []
	regex = 'umserver.log.201306*.bz2'
	for f in os.listdir(dir):
		if fnmatch.fnmatch(f,regex):
			#print f
			flist.append(f)

	for f in flist:
		print '正在处理%s...' % f
		fpath = os.path.join(dir,f)
		cmd1 = '''bzcat %s|grep '>>>>'|grep findpassword >> gxreset.log''' % fpath
		os.system(cmd1)

	print 'fuck gx over....'

def regexFile():
	f = '/data/logs/log_hjb/gxreset.log'
	fr = open(f,'r')
	num = 0
	result = []
	for line in fr:
		str = ''
		if line != None and len(line) > 0:
			#phone
			m = re.search(r'account=([\d]{11})',line)
			if m:
				phone = m.group(1)
				#print phone
				if phone ==None or len(phone) <= 0:
					continue
				str = phone
			#ip
			m = re.search(r'IP:([^,]*),',line)
			if m:
				ip = m.group(1)
				#print ip
				str += "|"+ ip
			#imei
			m = re.search(r'pub.CP_IMEI=([^,]*)',line)
			if m:
				imei = m.group(1)
				#print imei
				str += "|"+ imei
			#time
			index = line.index(',')
			time = line[0:index]
			str += "|" + time
			#uuid
			m = re.search(r'UUID:([^,]*),',line)
			if m:
				uuid = m.group(1)
				str += "|"+ uuid
		print str
		if str != None and len(str) > 0:
			result.append(str+"\n")
		#print num
		num += 1

	fresult = open('gxreset.txt','w')
	fresult.writelines(result)
	fresult.close()
	fr.close()
	print len(result)

getFiles()
regexFile()