#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#中国移动校园营销活动。客户端侧仅仅负责学分的同步，每天将前一天的用户学分同步给主平台
#设置一下字符编码
import os
import sys
import datetime as dt
import urllib
import urllib2

reload(sys)
sys.setdefaultencoding('utf-8')

#(datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y-%m-%d')

#常用参数
siteId = '111'#业务线ID
taskId = '11104'#任务ID
resourceId = '0'#资源ID
finishTime = ''#业务线授予学分时间,必须是yyyyMMddHHmmss格式。长度14位，不足14位，后面补“0”
source = '3'#来源,3:客户端
#validCode = '2013xiaoyuanjt'#接口验证口口令，活动正式开始后会有一个正式的口令
validCode = '050075bbe4a64a1ba0e3e814c6813c38'#现网正式口令
url = '''http://huodong.feixin.10086.cn:8081/xiaoyuan2013/Service.ashx?Action=UserTaskFinished'''#接口地址
#主平台host映射221.176.31.101 huodong.feixin.10086.cn
date_format = '%Y%m%d%H%M%S'
msg_receiver = '15210078395'#报警短信通知号码
wf_path = None#号码文件位置--声明为全局变量，打到可以在方法内部给这个变量赋值的目的
f_result = '/data/shell/mobile/result.txt'

#生成号码文件
from mobile import ParserMobiles
def parser():
	try:
		#测试代码，上线别忘了修改
		par = ParserMobiles()
		#在方法内部引用外部的变量时，必须采用global声明这个变量，然后再赋值
		global wf_path
		wf_path = par.parser()
	except Exception, e:
		msg = '生成号码文件失败：%s' % e
		print msg
		#send_sms(msg_receiver,msg)
	
#给主平台发送加分请求
def add_score(mobile):
	finishTime = get_str_time(date_format)
	print 'add score to %s at %s' % (mobile,finishTime)
	req = urllib2.Request(url,urllib.urlencode({"mobile":mobile,"siteId":siteId,"taskId":taskId,"resourceId":resourceId,"source":source,"finishTime":finishTime,"scoreCount":'2',"validCode":validCode}))
	#req = urllib2.Request(url,urllib.urlencode({"mobile":"15210078395","siteId":'111',"taskId":'11104',"resourceId":'0',"source":'3',"finishTime":finishTime,"scoreCount":'2',"validCode":'2013xiaoyuanjt'})) 
	resp = urllib2.urlopen(req)
	msg = 'sync %s to cmcc result:%s' % (mobile,resp.read())
	print msg
	return msg

#加载号码文件
def load_login_user():
	print 'load mobiles from local mobile file on the disk'
	login_users = ['15210078395']#一个空的列表，用来保存登录用户

	try:
		print '=========',wf_path
		if wf_path != None:
			f = open(wf_path,'r')
			for phone in f:
				if phone != None and len(phone) > 0:
					login_users.append(phone)
			#最后别忘了关闭文件
			f.close()
	except Exception, e:
		print 'excetion when read file %s :' % wf_path
	finally:
		print 'totally load %d mobiles' % (len(login_users))

	return login_users

#发送通知短信	
def send_sms(mobile,msg):
	sms_url = '''http://msgw.intra.umessage.com.cn:7000/sms/single?UserName=cilentsearch&Password=fkeiwour384729&AppCode=15100002&ReceiveType=2&SourceTermID=10658880&DestTermID=%s&FeeTermID=%s&MessageContent=%s''' % (mobile,mobile,msg)
	req = urllib2.Request(sms_url)
	resp = urllib2.urlopen(req)
	print 'send_sms %s result %s' % (sms_url,resp.read())

#开始同步给主平台
def sync(users):
	if users != None and len(users) > 0:
		yesterday =  get_yesterday_str_time('%Y-%m-%d',1)#格式化昨天的日期
		stime = dt.datetime.now()
		try:
			#====开始同步，下发通知短信==========
			msg = '开始给主平台同步[%s]日的登录用户，共[%d]条记录' % (yesterday,len(users))
			print msg
			send_sms(msg_receiver,msg)
		except Exception, e:
			print 'send msg:[%s] exception: %s' % (msg,e)
		
		#计数器，记录成功同步给主平台的用户数量
		file_result = open(f_result,'w')
		#接口返回的结果数组
		result_list = []
		count = 0
		try:
			result_list.append('=======%s=========\n' % yesterday)
			for mobile in users:
				#同步主平台并且记录返回结果
				result_list.append(add_score(mobile))
				count += 1

			result_list.append('=======%s=========\n' % yesterday)
		except Exception, e:
			print 'exception when sync to cmss: %s' % e
		finally:
			pass
		
		#写入同步日志，并且关闭文件流
		file_result.writelines(result_list)
		file_result.close()

		etime = dt.datetime.now()
		waste_seconds = (etime - stime).seconds
		try:
			#====同步完毕，下发通知短信==========
			msg2 = '同步给主平台[%s]日的登录用户完毕，共成功同步[%d]条记录，耗时[%d]秒' % (yesterday,count,waste_seconds)
			print msg2
			send_sms(msg_receiver,msg2)
		except Exception, e:
			print 'send msg:[%s] exception: %s' % (msg2,e)

		
#返回yyyyMMddHHmmss格式的时间
def get_str_time(strf = date_format):
	return dt.datetime.now().strftime(date_format)

#获取指定日期固定格式的时间
def get_yesterday_str_time(strf,inter = 1):
	return (dt.datetime.now()-dt.timedelta(days = inter)).strftime(strf)

if __name__ == '__main__':
	#解析昨天日志
	parser()
	#加载昨天的登录用户列表
	users = load_login_user()
	if users != None and len(users) > 0:
		sync(users)#依次同步给主平台
	else:
		print '...the list of login users is empty,do not sync to cmcc...'
