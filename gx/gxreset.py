#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:gxreset.py
import os
import xlwt

'''生成2013年6月份找回密码详情表格，手机号码、时间、归属地、串号、IP'''
dir = os.path.dirname(os.path.abspath(__file__))

mobileDict = {}
def mobileGs():
	segPath = os.path.join(dir,'mobile_segs.txt')
	seglist = open(segPath,'r').readlines()
	for item in seglist:
		key = item.split('=')[0]
		value = item.split('=')[1]
		mobileDict[key] = value

	print '共加载号段 %d 条' % (len(mobileDict))

def generate():
	path = os.path.join(dir,'gxreset.txt')
	resetlist = open(path,'r').readlines()
	wb = xlwt.Workbook('utf-8')
	ws = wb.add_sheet('2013年6月份客户端找回密码详情')
	num = 0
	ws.write(num,0,'手机号码')
	ws.write(num,1,'时间')
	ws.write(num,2,'城市')#城市
	ws.write(num,3,'省份')#省份
	ws.write(num,4,'串号')
	ws.write(num,5,'IP地址')

	for item in resetlist:
		num += 1
		arr = item.split('|')
		ws.write(num,0,arr[0])
		ws.write(num,1,arr[3])

		key = arr[0][0:7]
		if mobileDict.has_key(key):
			gs = mobileDict[key]
		else:
			gs = '未知&未知'
		ws.write(num,2,gs.split('&')[0])#城市
		ws.write(num,3,gs.split('&')[1])#省份

		ws.write(num,4,arr[2])
		ws.write(num,5,arr[1])

	final = os.path.join(dir,'2013年6月份客户端找回密码详情.xls')
	wb.save(final)


mobileGs()
generate()