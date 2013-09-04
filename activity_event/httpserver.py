#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Filename:httpserver.py
#一个简单的httpserver:启动9999端口，监听服务器发送来的生成活动页面的请求

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import urlparse
import generate_html as GH
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#SimpleHTTPRequestHandler只是可以当作文件服务器使用

#这个一个继承的类。BaseHTTPRequestHandler类似于JAVA中的抽象类，不可以直接使用，需实现一个子类并且实现do_GET或者do_POST方法才可以
class TestHTTPHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		#path = '/home/licb/active_template.html'
		path = '/usr/local/umclient/Tomcat_WWW/webapps_web/ROOT/activity/active_template.html'
		req = urlparse.urlparse(self.path)
		qs = urlparse.parse_qs(req.query)
		print '用户传入的参数为: %s' % qs

		if len(qs) > 0:
			ids = qs['id']
			if ids != None and len(ids) > 0:
				event_id = ids[0]
				print '生成[%s] 的活动页面' % event_id

				try:
					eid = int(event_id)
					GH.generate_event_html(path,eid)
				except Exception, e:
					#print '生成活动模板页面异常 %s ' % e
					pass
				finally:
					pass
		else:
			print '没有传入活动ID，直接跳过'

		buf = "It works"
		self.protocal_version = 'HTTP/1.1'
		self.send_response(200)
		self.send_header("Welcome", "Contect")
		self.end_headers()
		self.wfile.write(buf)

	def do_POST(self):
		do_GET()

def start_server(port):
	#不限定访问IP地址
	#allow_ips = ('172.16.80.110','172.16.80.111','172.16.80.130','172.16.80.131')
	http_server = HTTPServer(('', int(port)), TestHTTPHandler)
	#设置一直监听并接收请求
	http_server.serve_forever()

def stop_server(server):
    server.socket.close()

if __name__ == '__main__':
	start_server('9999')