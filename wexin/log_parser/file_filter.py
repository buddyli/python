#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:file_filter.py
#作用：接收用户指定的目录和正则表达式，返回目录中符合规定条件的文件的列表
import os
import fnmatch

class file_filter:
	"""文件过滤器：接收用户指定的目录和正则表达式，返回目录中符合规定条件的文件的列表"""
	#类初始化的方法，类似于java中的构造器
	def __init__(self):
		pass

	#self参数是为了本类的实例可以调用这个方法
	def filter(self,dir,regex):
		#保存该目录下符合条件的文件列表
		_files = [];
		try:
			for f in os.listdir(dir):
				if fnmatch.fnmatch(f,regex):
					_files.append(f)
		except Exception, e:
			print 'Error while list [%s] ,msg: %s' % (dir,e)
		finally:
			pass

		return _files

	#可以传入一个保存文件名称正则的列表，本方法会遍历指定的目录，并返回这些符合条件的文件
	def filter_multi_regex(self,dir,regexes):
		_files = []
		try:
			_all_files = os.listdir(dir)
			if len(_all_files) > 0:
				print 'there are %d files totaly' % len(_all_files)
				#为了实现这个功能使用了双层循环，这个不经济啊
				for reg in regexes:
					for tmp in fnmatch.filter(_all_files,reg):
						_files.append(tmp)
		except Exception, e:
			print 'Error while list [%s] ,msg: %s' % (dir,e)
		finally:
			pass

		return _files

ff = file_filter()
if __name__ == '__main__':
	#打印模块的说明文档
	#print ff.__doc__
	testdir = '/home/licb/documents/shells'
	testreg = '*.sh'
	testreglist = ['*.txt','*.sh']

	#_files = ff.filter(testdir,testreg)
	_files = ff.filter_multi_regex(testdir,testreglist)
	if len(_files) > 0:
		for f in _files:
			print os.path.abspath(f)
	else:
		print '''"%s" is a empty dir or there is no file like "%s"''' % (testdir,testreg)

		