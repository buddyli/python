#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import os
import re
import sys

'''
从wap的注册日志中提取注册帐号、ip地址、来源等字段
'''
flist = open('wap_reg.log','r').readlines()
fucklist = []
num = 0
for line in flist:
	str = ''
	m = re.search(r'account=([\d]{11})',line)
	if m:
		mobile = m.group(1)
		str += mobile
	else:
		continue

	m = re.search(r'(.*)- -',line)
	if m:
		ip = m.group(1)
		ip = ip.strip()
		str += ','+ip

	m = re.search(r'source=([\d]?)',line)
	if m:
		source = m.group(1)
		str += ','+source

	num += 1
	print '%d,%s' % (num,str)
	if len(str) > 0:
		fucklist.append(str+'\n')

fo = open('wap_imei.txt','w')
fo.writelines(fucklist)
fo.close()
