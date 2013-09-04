#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:gxxls.py
import os
import sys
import xlwt
from imei_ip import ImeiIP
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
class GxXls(object):
	"""他妈的广西数需要添加IP地址和IMEI重新生成表格"""
	oriCsv = 'gx2_0823.csv'
	regCsv = 'wap_reg_imeiandip.txt'
	clientRegCsv = 'client_reg.txt'
	csvList = []
	wapRegDict = {}
	clientRegDict = {}
	imeiObj = None
	def __init__(self):
		super(GxXls, self).__init__()
		#推荐记录加载进dict中
		self.imeiObj = ImeiIP()
		self.loadCsv()
		self.loadWapRegIp()
		self.loadClientReg()

	def loadCsv(self):
		self.csvList = open(self.oriCsv,'r').readlines()
		print '共加载推荐记录 %d 条' % len(self.csvList)

	#加载wap注册日志
	def loadWapRegIp(self):
		regList = open(self.regCsv,'r').readlines()
		for line in regList:
			line = line.replace('\n','')
			arr = line.split(',')
			if not self.wapRegDict.has_key(arr[0]):
				self.wapRegDict[arr[0]] = arr[1]

		print '共加载WAP注册记录 %d 条' % len(self.wapRegDict)

	#加载客户端注册日志，客户端注册日志是包括ip和imei号码的
	def loadClientReg(self):
		clientRegList = open(self.clientRegCsv,'r').readlines()
		for line in clientRegList:
			line = line.replace('\n','')
			#手机号码、Ip地址、串号
			arr = line.split('|')
			if not self.clientRegDict.has_key(arr[0]):
				value = arr[1] + ','
				if len(arr) == 3 and arr[2] != None:
					value += arr[2]

				self.clientRegDict[arr[0]] = value
		print '共加载客户端注册记录 %d 条' % len(self.clientRegDict)

	#获取用户在客户端的注册记录
	def getClientRegItem(self,key):
		if self.clientRegDict.has_key(key):
			value = self.clientRegDict[key].split(',')
			return value
		else:
			return None

	#获取用户在wap的注册记录
	def getWapRegItem(self,key):
		if self.wapRegDict.has_key(key):
			value = self.wapRegDict[key].split(',')
			return value
		else:
			return None

	def writeToXls(self):
		wb = xlwt.Workbook('utf-8')
		total = len(self.csvList)
		page_size = 50000
		start_index = 0

		sheet_num = 1
		while start_index < total:
			#list截取字串是[,)形式的，一定要注意
			end_index = start_index + page_size
			print '%s----处理从%d到%d的记录。。。' % (datetime.now().strftime(DATE_FORMAT),start_index,end_index)

			if end_index > total:#如果剩余不足5W条记录，获取剩余所有的记录
				tmplist = self.csvList[start_index:]
			else:
				tmplist = self.csvList[start_index:end_index]

			sheet_name = '第%d页' % (sheet_num)
			sheet_num += 1
			ws = wb.add_sheet(sheet_name)	
			num = 0
			ws.write(num,0,'推荐用户')
			ws.write(num,1,'推荐用户归属地')
			ws.write(num,2,'省份')
			ws.write(num,3,'推荐时间')
			ws.write(num,4,'推荐用户IMEI')
			ws.write(num,5,'推荐用户IP')
			ws.write(num,6,'被推荐用户')
			ws.write(num,7,'被推荐用户归属地')
			ws.write(num,8,'省份')
			ws.write(num,9,'被推荐用户IMEI')
			ws.write(num,10,'被推荐用户IP')
			ws.write(num,11,'注册来源')
			ws.write(num,12,'注册时间')
			ws.write(num,13,'激活时间')
			
			for item in tmplist:
				num += 1
				arr = item.split(',')
				if len(arr) == 1:
					arr = item.split('\t')

				ws.write(num,0,arr[0])
				ws.write(num,1,arr[1])
				ws.write(num,2,arr[2])
				ws.write(num,3,arr[3])

				key = arr[0] + '-' + arr[4]
				imeiIp = self.imeiObj.getImeiAndIPFromDict(key)
				if imeiIp != None and len(imeiIp) > 0:
					imeiArr = imeiIp.split(',')
					ws.write(num,4,imeiArr[1])
					ws.write(num,5,imeiArr[0])
				else:
					ws.write(num,4,'')
					ws.write(num,5,'')

				ws.write(num,6,arr[4])
				ws.write(num,7,arr[5])
				ws.write(num,8,arr[6])

				#计算激活时间和注册时间的差值
				active = arr[9].replace('\n','')
				active = active.replace('\r','')
				if arr[8] != '\N' and active != '\N':
					dtReg = datetime.strptime(arr[8],DATE_FORMAT)
					dtActive = datetime.strptime(active,DATE_FORMAT)
					diff = (dtActive - dtReg).seconds

				regIp = self.getWapRegItem(arr[4])
				#如果用户没有注册话，注册的IMEI和IP字段不用添加
				#注册来源为0，是用户手动从wap页面注册，没有记录用户注册IP地址
				if arr[7] == '1':
					if arr[8] != '\N':
						#在客户端注册但是没有激活的也要有截图
						if active == '\N' or diff > 3:
							regIp = self.getClientRegItem(arr[4])
							if regIp == None:
								print '%s 没有在客户端注册' % item
								continue
							else:
								ws.write(num,10,regIp[0])#IP
								ws.write(num,9,regIp[1])#IMEI
				elif arr[7] != '0' and arr[8] != None and arr[8] != '\N' and regIp != None and len(regIp) > 0:
					ws.write(num,10,regIp[0])
					ws.write(num,9,'')
				else:
					ws.write(num,10,'')
					ws.write(num,9,'')

				ws.write(num,11,arr[7])#注册来源
				ws.write(num,12,arr[8])#注册时间
				ws.write(num,13,arr[9])#激活时间

			#开始位置向后移动
			start_index += page_size

		strtime = datetime.now().strftime(DATE_FORMAT)
		fname = 'gx_%s.xls' % strtime
		wb.save(fname)

obj = GxXls()
obj.writeToXls()