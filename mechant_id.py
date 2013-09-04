#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:mechant_id.py
#统计指定时间段内的用户请求的商户详情ID
import os
import bz2
import time
import re

#r表示正则中的任何字符串都没有特殊含义，这样的话就不用\再转了
regexp = re.compile(r'''^umserver.log.201302.+?bz2$''')
reg_merchantid = re.compile(r'''merchant_id=([^,]*)''')
strtime = time.strftime('%Y%m%d%H%M%S')
#grep 命令
cmd_grep = None
log_dir = '/data/logs/log_hjb'
fs = os.listdir(log_dir)
db = 'merchantdetail.db'#中间文件
db_id = 'merchant_id.db'#保存商户ID
db_result = 'merchant_id_sort.db'

print '遍历日志生成中间文件'
#遍历日志生成中间文件
if not os.path.exists(db):
	if len(fs) > 0:
		for f in fs:
			if regexp.search(f) is not None:
				cmd_grep = '''bzcat %s |grep ">>>>,UUID"''|grep "merchantdetail" >> %s''' % (f,db)
				os.system(cmd_grep)
else:
	print '中间日志已经存在，不用再次生成'
print '====生成中间日志完毕'

print '解析商户详情的请求，获取商户ID'
if os.path.exists(db) and os.path.isfile(db):
	file_entry = open(db,'r')
	file_id = open(db_id,'w')#append这个文件，而不是重写

	for line in file_entry:
		m = re.search(reg_merchantid,line)
		if m != None:
			if m.group(1) != None:
				print '%s ' % (m.group(1))
				s = m.group(1)+'\n'
				file_id.write(s)
	
	#关闭打开的文件
	#os.close(file_id)
	#os.close(file_entry)
print '====商户详情解析完毕'

print '对商户ID排序，去重'
cmd_sort = 'cat %s|sort|uniq -c|sort -r -n -k1,1 > %s' % (db_id,db_result)
if os.system(cmd_sort) == 0:
	print '商户ID排序完毕'
print '====排序后的商户ID输出完毕'
		
