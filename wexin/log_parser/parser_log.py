#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:parser_log.py
import bz2
import os
import time
import string

class parser_log:
	#需要生成的三个临时文件
	cmd_entry = None#所有请求进入的日志
	cmd_flow_up = None#上行日志
	cmd_flow_down = None#下行日志
	FLOW_UP = {}#上行日志字典
	FLOW_DOWN = {}#下行日志字典
	REQ_ENTRY = {}
	#%Y%m%d%H%M%S: 年月日时分秒格式
	#file_suffix = time.strftime('%Y%m%d')
	
	def __init__(self):
		#初始化抓取各个字段的正则
		self.CP_CH = 'pub.CP_CH=(.*?),?'  #渠道
        self.CP_CITYID = 'pub.CP_CITYID=(.*?),?' #城市ID
        self.CP_IMEI = 'pub.CP_IMEI=(.*?),?' #串号
        self.CP_MODEL = 'pub.CP_MODEL=(.*?),?' #手机型号
        self.CP_PLTFM = 'pub.CP_PLTFM=(.*?),?' #手机平台
        self.CP_PRT = 'pub.CP_PRT=(.*?),?' #手机产品号 !important
        self.CP_RATIO = 'pub.CP_RATIO=(.*?),?' #手机分辨率
        self.CP_TOUCH = 'pub.CP_TOUCH=(.*?),?' #是否触摸屏
        self.CP_UID = 'pub.CP_UID=(.*?),?' #用户ID--登陆用户标示
        self.CP_VER = 'pub.CP_VER=(.*?),?' #平台版本 
        self.CP_PHONENUM = 'pub.CP_PHONENUM=(.*?),?' #手机号
        self.CP_TPL = 'pub.CP_TPL=(.*?),?' #手机适配模板类型
        self.CP_RESVER = 'pub.CP_RESVER=(.*?),?' #资源版本号
        self.CP_PUBRESPATH = 'pub.CP_PUBRESPATH=(.*?),?' #公共资源路径- cache路径
        self.CP_LON = 'pub.CP_LON=(.*?),?' #手机经
        self.CP_LAT = 'pub.CP_LAT=(.*?),?' #手机维度
        self.UUID = 'requuid=(.*?),?' #请求UUID
        self.ACTION = 'REQ_ACTION:(.*?),?' #请求的Action
        self.IP = 'IP:(.*?),?' #请求地址
        self.TIME = None #访问时间，这个字段需要截取字符串来获取[0,23)
		self.file_suffix = time.strftime('%Y%m%d')
	#格式化完整的grep语句，并生成中间文件
	def generate_middle_file(self,fn):
		#%Y%m%d%H%M%S: 年月日时分秒格式
		#file_suffix = time.strftime('%Y%m%d')
		cmd_entry = '''bzcat %s|grep ">>>>,UUID">%s_all.txt''' % (fn,file_suffix)
		cmd_flow_up = '''bzcat %s|grep "====FLOW_UP">%s_up.txt''' % (fn,file_suffix)
		cmd_flow_down = '''bzcat %s|grep "====FLOW_DOWN">%s_down.txt''' % (fn,file_suffix)

		try:
			os.system(cmd_entry)
			os.system(cmd_flow_up)
			os.system(cmd_flow_down)
		except Exception, e:
			print 'run generate_middle_file Exception: %s' % e
		finally:
			print 'generate_middle_file of %s success' % file_suffix

	#解析中间文件，将上下行日志以uuid为主键放入字典中
	def parser_middle_file(self):
		#file_suffix = time.strftime('%Y%m%d')
		f_all = open('%s_all.txt' % file_suffix,'r')
		'''====FLOW_UP|9890c88a-8e52-11e2-be87-00ea011120c8|476efb2b970a49b2c7b4eb0046746b||737|SHA002A02600'''
		'''====FLOW_DOWN|9ac34880-8e52-11e2-a220-00241d92c6c0|b5adfb2b970a49b2c7b4eb0046746b||177||251'''
		'''>>>>,UUID:97d47ff3-8e52-11e2-bd72-00ea011120c8,IP:58.221.47.247,REQ_ACTION:searchandrange,REDIRECT_URL:http://localhost:9090/searchandrange,PARAMS:{pub.CP_TOUCH=1, pub.CP_PRT=SHA002A02600, type=<E6><88><90><E4><BA><BA><E6><95><99><E8><82><B2>, pub.CP_RATIO=480*854, linename=101, city_id=21040000, distance=, pub.CP_LAT=, action=searchandrange, pub.CP_CH=A002, lat=, pub.CP_MODEL=MI-ONE-Plus, pub.CP_IMEI=4015fb2b970a49b2c7b4eb0046746b, requuid=97d47ff3-8e52-11e2-bd72-00ea011120c8, pub.CP_PLTFM=android, lon=, standard=84, pub.CP_LON=, keyword=, pub.CP_PHONENUM=, mark=2, pub.CP_TPL=, pub.CP_VER=Android4.1.1, trade_name=, pub.CP_RESVER=1.0, pub.CP_PUBRESPATH=file:///android_asset/more/public, pub.CP_CITYID=20010000, pub.CP_UID=}'''
		f_up = open('%s_all.txt' % file_suffix,'r')
		f_down = open('%s_all.txt' % file_suffix,'r')
		try:
			for line in f_up:
				arr = line.split('|')#返回一个列表
				FLOW_UP[arr[1]] = line

			for line in f_down:
				arr = line.split('|')
				FLOW_DOWN[arr[1]] = line

		finally:
			print '=====parse middle file over===='
			f_up.close()
			f_down.close()
		 	f_all.close() 

if __name__ == '__main__':

