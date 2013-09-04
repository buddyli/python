#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import re

class ImeiIP(object):
	"""
	将客户端的推荐记录组装成字典
	key:推荐号码-被推荐号码
	value:ip,串号
	"""
	imeiList = []
	inviteDict = {}
	def __init__(self):
		super(ImeiIP, self).__init__()
		self.loadImei()
		
	def loadImei(self):
		self.imeiList = open('invite_detail.txt','r').readlines()
		print '共加载推荐记录[%d]条' % len(self.imeiList)
		for item in self.imeiList:
			item = item.replace('\n','')
			item = item.replace('\r','')
			arr = item.split('|')
			invited = arr[3]
			invitedArr = arr[3].split(',')
			#IP,IMEI
			value = arr[1]+","+arr[2]
			if len(invitedArr) == 0:
				continue

			for mo in invitedArr:
				m = re.search(r'(\+?86)?(?P<phone>[\d]{11})',mo)
				if m:
					phone = m.group('phone')
					#print '%s-%s' % (mo,phone)
				key = arr[0]+'-'+phone
				#如果该条记录在dict中不存在，那么加入字典中
				self.add2Dict(key,value)

		print '======= %d' % len(self.inviteDict)

	def add2Dict(self,key,value):
		try:
			#如果已经在字典中，不用重复添加
			if self.inviteDict.has_key(key):
				pass
			else:
				self.inviteDict[key] = value
		except Exception, e:
			print e

	def getRecordByMobile(self,inviter,invited):
		for item in self.imeiList:
			if item.startswith(inviter) and item.find(invited) != -1:
				return item
			else:
				continue

	#从dict中获取邀请记录
	def getImeiAndIPFromDict(self,key):
		if self.inviteDict.has_key(key):
			return self.inviteDict[key]
		else:
			return None


if __name__ == '__main__':
	obj = ImeiIP()
	print obj.getImeiAndIPFromDict('18378224924-13768015121')
	print obj.getImeiAndIPFromDict('18378224924-13768524414')
