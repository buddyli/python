#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:gxreset_sms.py
import os
import re
from urllib import quote,unquote

"""
捞取广西6月重置密码的数据
"""
def loadFiles():
	fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'c.txt')
	print fpath
	smsList = open(fpath,'r')
	result = []

	num = 0
	for item in smsList:
		num += 1
		print num
		m = re.search(r'DestTermID=(?P<phone>[\d]{11})',item)
		if m:
			phone = m.group('phone')

		m = re.search(r'MessageContent=.+?(?P<passwd>[a-z0-9]{6}).+',item)
		if m:
			passwd = m.group('passwd')

		print '%s,%s' % (phone,passwd)
		result.append(phone+','+passwd+'\n')

	f = open('passwd.txt','w')
	f.writelines(result)

loadFiles()