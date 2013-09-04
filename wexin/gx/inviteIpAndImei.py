#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#inviteIpAndImei.py
import re

"""
从活动期间推荐日志提取推荐号码、被推荐号码、IP和IMEI

以前提取的正则中，判断手机号码的正则有问题，没有将+86这种国标码考虑进去，导致有些记录没有提取出来
invite_imie_ip.txt做为参考，以后不用再次使用了。
"""

inviteLog = 'client_invite_grep.log'
def loadToList():
	return open(inviteLog,'r').readlines()

def parserLog():
	inviteList = loadToList()
	rList = []
	for str in inviteList:
		#phone
		m = re.search(r'pub.CP_PHONENUM=([\d]{11})',str)
		if m:
			phone = m.group(1)
			#print phone
			if phone ==None or len(phone) <= 0:
				print 'fuck'

			result = phone
			#print result
		#ip
		m = re.search(r'IP:([^,]*),',str)
		if m:
			ip = m.group(1)
			#print ip
			result += "|"+ ip
			#print result
		#imei
		m = re.search(r'pub.CP_IMEI=([^,]*)',str)
		if m:
			imei = m.group(1)
			#print imei
			result += "|"+ imei
			#print result
		#invite
		m = re.search(r'invit_number=([^a-zA-Z]*),',str)
		if m:
			invite = m.group(1)
			print invite
			result += "|"+ invite
			#print result

		result += '\n'
		rList.append(result)

	open('invite_detail.txt','w').writelines(rList)

parserLog()