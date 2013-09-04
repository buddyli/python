#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

class LoadMobileSeg(object):
	"""加载号段文件到字典中"""
	seg_path = None
	def __init__(self, seg_path):
		super(LoadMobileSeg, self).__init__()
		self.seg_path = seg_path

	def load(self):
		'''读取号段文件，将号段文件放到字典中，形式为"1390130=北京&北京市"'''
		seg_dict = {}
		if self.seg_path == None or not (os.access(self.seg_path,os.F_OK)):
			print '请输入正确的号段文件路径...'
			sys.exit(0)

		f = open(self.seg_path,'r')
		for line in f:
			if line != None:
				key = line.split('=')[0]
				value = line.split('=')[1]
				seg_dict[key] = value
		f.close()
		
		return seg_dict

class LoadInvite(object):
	'''加载所有的推荐记录到内存中'''
	def __init__(self,fpath,fresult):
		super(LoadInvite, self).__init__()
		self.fpath = fpath
		self.fresult = fresult

	def load(self):
		'''加载所有的推荐记录
		注意：推荐记录中有推荐号码为空的记录，这些记录直接去掉不处理。
		将推荐号码和被推荐号码加上号码归属地字段后，拼接到一个新的list中并返回。
		'''
		list_result = []
		if self.fpath == None or not os.access(self.fpath,os.F_OK):
			print '推荐记录文件不存在，请检查路径。。。'
			sys.exit(0)

		#加载号段文件
		lms = LoadMobileSeg('/home/licb/segs.txt')
		seg_dict = lms.load()
		#加载推荐记录
		f = open(self.fpath,'r')
		#使用追加模式写入目标文件
		result = open(self.fresult,'a')
		rlist = []
		for line in f:
			invite = line.split('\t')
			if invite[0] == None or len(invite[0]) == 0:
				print '推荐号码为空，不处理本条记录。。。'
				continue;

			#推荐用户、推荐时间、归属地、被推荐用户、归属地、来源、注册时间、激活时间
			try:
				gsd1 = seg_dict[invite[0][0:7]]
			except Exception, e:
				gsd1 = '未知&未知'

			try:
				gsd2 = seg_dict[invite[1][0:7]]
			except Exception, e:
				gsd2 = '未知&未知'
			
			str = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (invite[0],gsd1.split('&')[0],gsd1.split('&')[1],invite[2],invite[1],gsd2.split('&')[0],gsd2.split('&')[1],invite[5],invite[3],invite[4])
			str = str.replace('\n','')
			str = str + '\n'
			rlist.append(str)
			print str
		
		result.writelines(rlist)

		f.close()
		result.close()

if __name__ == '__main__':
	#lms = LoadMobileSeg('/home/licb/segs.txt')
	#seg_dict = lms.load()
	#print len(seg_dict)
	#print seg_dict['1521007']

	objLi = LoadInvite('/home/licb/all.csv','/home/licb/fuckgx_new.csv')
	objLi.load()
