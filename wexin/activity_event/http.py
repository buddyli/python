#!/usr/bin/evn python
#-*- encoding:utf-8 -*-
#Filename:http.py
#用来包装http请求的工具类

import httplib,urllib
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class Http:
	"""用来包装http请求的工具类"""
	def __init__(self, host,port):
		self._host = host
		self._port = int(port)
		self._conn = None
		self._headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

	#发送普通的http请求,host,port,headers不传入使用默认值
	def request(self,url,data = None,host = None,port = None,headers = None):
		#响应
		ret = None
		#创建链接
		if self._conn == None:
			self._conn = httplib.HTTPConnection(host or self._host, port or self._port)

		#执行请求
		#self._conn.request('POST','/wapcms/wap/web_online_xml.php',data,headers or self._headers)
		self._conn.request('POST',url,data,headers or self._headers)
		#获取响应
		response = self._conn.getresponse()
		if response.status == 200 and response.reason == 'OK':
			ret = response.read()
		else:
			print '请求cms生成活动模板异常 %d %s' % (response.status,response.reason)

		return ret

	#返回格式化好的参数列表
	def getparams(self,dict):
		return urllib.urlencode(dict)

#测试主函数
if __name__ == '__main__':
	http = Http('172.16.18.155',7777)
	#para = {'act':'xml','id':'27'}
	#data = http.getparams(para)
	url = '%s%d' % ('/wapcms/wap/web_online_xml.php?id=',27)
	print http.request(url,None)