#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:register_imei_ip.py
#统计指定时间段内的注册用户的IMEI和IP
import os
import bz2
import time
import re

#r表示正则中的任何字符串都没有特殊含义，这样的话就不用\再转了
regexp = re.compile(r'''^umserver.log.201306.+?bz2$''')
reg_imei = re.compile(r'''CP_IMEI=([^,]*)''')
reg_ip = re.compile(r'''IP:([^,]*)''')
#account
reg_mobile = re.compile(r'''account=([^,]*)''')
strtime = time.strftime('%Y%m%d%H%M%S')
#grep 命令
cmd_grep = None
log_dir = '/data/logs/log_hjb'
fs = os.listdir(log_dir)
db = 'register_imei_ip.db'#中间文件
db_id = 'final_register.db'#保存注册用户的IMEI和IP
db_result = 'final_register_sort.db'

#第一步，遍历2013年6月份的全部日志，获取所有注册请求
print '遍历日志生成中间文件'
#遍历日志生成中间文件
if not os.path.exists(db):
	if len(fs) > 0:
		for f in fs:
			if regexp.search(f) is not None:
				print '===处理日志文件 %s' % f
				cmd_grep = '''bzcat %s |grep ">>>>,UUID"''|grep "register" >> %s''' % (f,db)
				os.system(cmd_grep)
else:
	print '中间日志已经存在，不用再次生成'
print '====生成中间日志完毕'

#第二步，从用户的注册请求中解析出用户手机号码,IMEI和IP，将这三个字段存入db_id中，用来给下一步的去重操作做为输入文件用
print '解析用户请求，获取用户注册时的IMEI和IP'
if os.path.exists(db) and os.path.isfile(db):
	file_entry = open(db,'r')
	file_id = open(db_id,'w')#append这个文件，而不是重写

	for line in file_entry:
		#需要提取的三个字段
		imei = None
		mobile = None
		ip = None

		#imei
		m1 = re.search(reg_imei,line)
		if m1 != None:
			if m1.group(1) != None:
				print '%s ' % (m1.group(1))
				imei = m1.group(1)

		#ip
		m2 = re.search(reg_ip,line)
		if m2 != None:
			if m2.group(1) != None:
				print '%s ' % (m2.group(1))
				ip = m2.group(1)

		#mobile
		m3 = re.search(reg_mobile,line)
		if m3 != None:
			if m3.group(1) != None:
				print '%s ' % (m3.group(1))
				mobile = m3.group(1)

		str_line = '%s,%s,%s\n' % (mobile,imei,ip)
		file_id.write(str_line)
	
	#关闭打开的文件
	file_entry.close()
	file_id.close()
print '====解析用户注册请求完毕'

#第三步，将上一步获取到的文件排序，去重，只保留用户第一次注册时的IMEI和IP
print '对用户注册IMEI和IP，去重'
cmd_sort = 'cat %s|sort|uniq > %s' % (db_id,db_result)
print 'execute %s' % cmd_sort
if os.system(cmd_sort) == 0:
	print '用户注册IMEI和IP去重完毕'
print '====排序后的用户注册IMEI和IP输出完毕'
		
