#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#import threading
import urllib
import urllib2
import threading
import datetime

global siteId
siteId = '111'#业务线ID
global taskId
taskId = '11104'#任务ID
global resourceId
resourceId = '0'#资源ID
global source
source = '3'#来源,3:客户端
global validCode
validCode = '2013xiaoyuanjt'#接口验证口口令，活动正式开始后会有一个正式的口令
global url
url = '''http://huodong.feixin.10086.cn:8081/xiaoyuan2013/Service.ashx?Action=UserTaskFinished'''#接口地址
date_format = '%Y%m%d%H%M%S'

class SyncThread(threading.Thread):
	finishTime = None
	def __init__(self,mobile):
		self._phone = mobile
		threading.Thread.__init__(self)

	def run(self):
		finishTime = datetime.datetime.now().strftime(date_format)
		print 'add score to %s at %s' % (self._phone,finishTime)
		req = urllib2.Request(url,urllib.urlencode({"mobile":self._phone,"siteId":siteId,"taskId":taskId,"resourceId":resourceId,"source":source,"finishTime":finishTime,"scoreCount":'2',"validCode":validCode}))
		resp = urllib2.urlopen(req)
		print 'sync %s to cmcc result:%s' % (self._phone,resp.read())

if __name__ == '__main__':
	thread = SyncThread('15210078395')
	thread.start()
