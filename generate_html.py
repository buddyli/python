#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:generate_html.py
#读取接口，获取活动内容，然后套入活动模板中，生成完整的活动页面供客户端调用
import sys,os
from http import Http
import xml.dom.minidom
from xml.dom.minidom import parseString,parse
import xml.etree.ElementTree as ET

reload(sys)
sys.setdefaultencoding('utf-8')

#生成嵌套后的模板文件(event_id.html)
def generate_event_html(path,event_id):
	html = get_template(path)
	ret = get_event_content(event_id)

	if ret == None:
		print '请求cms接口获取到的活动内容为空'
	else:
		print 'cms返回的活动内容为: %s ' % ret

	#嵌套模板CSS样式不好使用，这里不再嵌套，而是直接显示cms返回的内容
	#html = html.replace('#content_from_cms#',ret)
	html = ret

	dir_name = os.path.dirname(path)
	fname = '%d%s' % (event_id,'.html')
	fname = os.path.join(dir_name,fname)
	head = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
	<title></title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
 </head>
<body>'''
	end = '''</body></html>'''
	try:
		#if os.path.exists(fname):
		#	os.remove(fname)

		f = file(fname,'w')
		f.write(head)
		f.write(html)
		f.write(end)
		f.close()
	except Exception, e:
		#print '生成活动页面异常:%s' % e
		pass
	finally:
		pass

	return fname

#请求cms接口获取文件内容，需要解析下面节点的content字段去显示
'''<field>
<id>26</id>
<title>
<![CDATA[ 李传宝测试活动内容 ]]>
</title>
<content>
<![CDATA[ <strong>中国人民大团结万岁</strong> ]]>
</content>
</field>'''
def get_event_content(event_id):
	#os.system('''export http_proxy=""''')
	print '获取id为[%d]的活动内容' % event_id

	http = Http('plogin.12580.com',80)
	#para = {'act':'xml','id':event_id}
	#req_para = http.getparams(para)
	url = '%s%d' % ('/cmps/wapcms/wap/web_online_xml.php?id=',event_id)
	ret = http.request(url)

	#解析返回的xml报文
	#om = parseString(ret)
	#field_node = dom.documentElement
	#content_node = field_node.getElementsByTagName('content')[0]

	#data = None
	#if content_node.nodeType in (content_node.TEXT_NODE,content_node.CDATA_SECTION_NODE):
	#	data = content_node.data
	#else:
	#	print content_node.nodeType
	print 'cms返回报文: %s ' % ret

	root = ET.fromstring(ret)
	msg = {}
	for node in root:
		msg[node.tag] = node.text

	data = msg['content']
	print 'cms返回的活动内容为:%s' % (data or 'cms返回空')

	#os.system('''export http_proxy="http://127.0.0.1:8087/"''')
	return data

#获取模板文件内容
def get_template(path = None):
	content = None
	if path == None:
		path = ''#默认路径

	try:
		#读取模板文件内容
		template = open(path,'r')
		for line in template:
			content = '%s%s' % (content,line)
	except Exception, e:
		print '打开模板文件失败，请检查配置:%s' % e
		sys.exit(0)
	finally:
		print '读取模板文件[%s]内容成功' % path

	return content

if __name__ == '__main__':
	path = '/home/licb/active_template.html'
	html = generate_event_html(path,27)
	print html