#!/usr/bin/evn python
#-*- encoding:utf-8 -*-
import os
import re

str = '''2013-06-30 22:33:03,003-[TS] INFO http-9090-Processor com.umessage.splat.web.servlet.ClientEntranceServlet - >>>>,UUID:cfda5933-0e9e-4f8a-b394-f429b4d885ed,IP:117.136.14.83,REQ_ACTION:invatation,REDIRECT_URL:http://localhost:9090/invatation,PARAMS:{pub.CP_PLTFM=ANDROID, pub.CP_TOUCH=1, pub.CP_LON=108.31614, pub.CP_PHONENUM=13878848027, pub.CP_PRT=SHA001A02630, invit_number=13878848026,, pub.CP_TPL=android, pub.CP_RATIO=480*800, pub.CP_VER=Android4.0.4, pub.CP_LAT=22.845308, action=invatation, pub.CP_RESVER=1.0, user_id=400184474, pub.CP_IP=117.136.14.83, pub.CP_CITYID=29010000, pub.CP_CH=A001, pub.CP_PUBRESPATH=file:///android_asset/more/public, pub.CP_UID=400184474, pub.CP_MODEL=GT-S7568, pub.CP_IMEI=356209051726195, requuid=cfda5933-0e9e-4f8a-b394-f429b4d885ed}'''
result = ''
if str != None and len(str) > 0:
	#phone
	m = re.search(r'pub.CP_PHONENUM=([\d]{11})',str)
	if m:
		phone = m.group(1)
		#print phone
		if phone ==None or len(phone) <= 0:
			print 'fuck'

		result = phone
		print result
	#ip
	m = re.search(r'IP:([^,]*),',str)
	if m:
		ip = m.group(1)
		#print ip
		result += "|"+ ip
		print result
	#imei
	m = re.search(r'pub.CP_IMEI=([^,]*)',str)
	if m:
		imei = m.group(1)
		#print imei
		result += "|"+ imei
		print result
	#invite
	m = re.search(r'invit_number=(([\d]{11},?)+)',str)
	if m:
		invite = m.group(1)
		#print invite
		result += "|"+ invite
		print result
print result


item = "18778153790|221.7.250.136|860626002921790|15777173624,18778987244,18776897573,15994309360,15994306638,15994306220,13978621584,18776906836,"
#print item.startswith('18778153790')
#print item.find('15777173624')
#print item.find('fuck')
print '============='
#print '\n'
#print '\r'
print '\r\n'

inviteDict = {}
def add2Dict(key,value):
	try:
		#如果已经在字典中，不用重复添加
		if inviteDict.has_key(key):
			print 'fdffddfdfdfdf'
		else:
			print '添加。。。。'
			inviteDict[key] = value
	except Exception, e:
		print type(Exception)

add2Dict('fuck','value')
print inviteDict


print os.path.abspath(__file__)
print os.path.dirname(os.path.abspath(__file__))
print os.path.join(os.path.dirname(os.path.abspath(__file__)),'120new.csv')


for col in range(5):
	print col