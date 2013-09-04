#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#遍历日志，将每天的登录用户手机号码去重后写入中间文件
import datetime
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class ParserMobiles():
	"""遍历日志，将每天的登录用户手机号码去重后写入中间文件"""
	def __init__(self, rpath = '/data/logs/log_hjb/',wpath = '/data/shell/mobile/',flag_override = 1,strf = '%Y%m%d'):
		self.rpath = rpath#读取的源日志文件地址
		self.wpath = wpath#写入的目标文件地址
		self.datef = strf#格式化日期字符串样式
		self.flag_override = flag_override#如果目标文件已经存在，程序再次运行时，是否重新生成该文件标识。0:否；1：是。默认始终重新生成该文件
	
	def parser(self):
		"""
		解析前一天的日志文件，将所有登录用户的手机号码读取到文件中
		"""
		#拼装需要解析的日志文件名称
		rf_name = 'umserver.log.%s.bz2' % (self.get_file_suffix(1))
		rf_full_path = '%s%s' % (self.rpath,rf_name)
		print rf_full_path
		#拼装要写入的号码文件的名称
		wf_name = 'mobile_%s.txt' % (self.get_file_suffix(1))
		wf_full_path = '%s%s' % (self.wpath,wf_name)
		print wf_full_path

		try:
			#标记为1，每次都始终生成该中间文件
			if self.flag_override == 1:
				if os.path.exists(rf_full_path):
					cmd = '''bzcat %s|grep "====FLOW_UP"|awk -F'|' '{print $4}'|sort|uniq >%s''' % (rf_full_path,wf_full_path)
					os.system(cmd)
				else:
					print '日志源文件%s不存在，程序中止。' % rf_full_path
			elif os.path.exists(wf_full_path):#标记为0，如果有中间文件，将不再生成
				print '中间号码文件%s已经存在，根据系统策略，不再重新生成。' % wf_full_path
		except Exception, e:
			print e
			raise#用来引发异常
		finally:
			return wf_full_path

	def get_file_suffix(self,inter,datef = None):
		"""获取号码文件后缀"""
		if datef  == None:
			datef = self.datef

		return (datetime.datetime.now()-datetime.timedelta(days = inter)).strftime(datef)

pm = ParserMobiles('/home/licb/','/home/licb/',1)
if __name__ == '__main__':
	#print pm.get_file_suffix(1)
	pm.parser()

