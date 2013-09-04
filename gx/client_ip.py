#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:client_ip.py

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
		cmd = '''bzcat %s|grep '>>>>'|grep register|grep -v -e '2013-04-0[123456789]' >>gxreg.log''' % fpath
		os.system(cmd)

	print 'fuck gx over....'

def regexFile():
	f = '/data/logs/hjb/gxreg.log'
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
		print str
		if str != None and len(str) > 0:
			result.append(str+"\n")
		#print num
		num += 1

	fresult = open('gxreg.txt','w')
	fresult.writelines(result)
	fresult.close()
	fr.close()
	print len(result)

getFiles()
regexFile()