#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:ip.py
#用来将所有的IP段包含的IP地址拆分出来
import os
import sys
#重新设置系统编码
reload(sys)
sys.setdefaultencoding('utf-8')

fn = '/home/licb/00010.txt'
ips = '/home/licb/ips.txt'

def parser():
	f = open(fn,'r')
	f_result = open(ips,'w')

	#开始循环每个IP段
	for line in f:
		print '开始处理IP段 %s' % line
		#每个IP段拆分出的IP都保存在这个列表中
		result_list = []
		#16777472,16777727,24,0103,350000,9999
		#第3列是不用的
		ip_list = line.split(',')
		start_ip = ip_list[0]
		end_ip = ip_list[1]
		#起止IP转成整型
		start = int(start_ip)
		end = int(end_ip) + 1
		#遍历这个IP地址段，将所有的IP写入结果文件中
		for i in range(start,end):
			ip_str = '%d,%s,%s,%s' % (i,ip_list[3],ip_list[4],ip_list[5])
			print ip_str
			result_list.append(ip_str)

		#写入结果文件
		if len(result_list) > 0:
			f_result.writelines(result_list)

	#关闭打开的文件
	f.close()
	f_result.close()

if __name__ == '__main__':
	parser()