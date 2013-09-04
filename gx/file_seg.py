#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:file_seg.py
import os
import sys
import xlwt#用来写入excel表格的模块

reload(sys)
sys.setdefaultencoding('utf-8')

class SegFile(object):
	"""
	广西推荐明细共有88万多条记录，需分成多个sheet页面展示
	"""
	fpath = None
	def __init__(self, fpath):
		super(SegFile, self).__init__()
		self.fpath = fpath
		if self.fpath == None or not os.access(self.fpath,os.F_OK):
			print '目标文件路径%s不存在，程序退出...' % self.fpath
			sys.exit(0)

	def loadToList(self):
		"""加载目标文件到list中"""
		flist = []
		f = open(self.fpath,'r')
		for line in f:
			flist.append(line)

		f.close()
		return flist

	def writeToExcel(self,targetFile):
		"""将记录写入excel表格中，添加了对号码归属地的容错处理"""
		flist = self.loadToList()
		print '共需要导入%d条记录' % len(flist)
		
		total = len(flist)
		page_size = 50000
		start_index = 0

		wb = xlwt.Workbook('utf-8')
		sheet_num = 1
		while start_index < total:
			#list截取字串是[,)形式的，一定要注意
			end_index = start_index + page_size
			print '处理从%d到%d的记录。。。' % (start_index,end_index)

			if end_index > total:#如果剩余不足5W条记录，获取剩余所有的记录
				tmplist = flist[start_index:]
			else:
				tmplist = flist[start_index:end_index]

			sheet_name = '第%d页' % (sheet_num)
			sheet_num += 1

			ws = wb.add_sheet(sheet_name)
			num = 0
			ws.write(num,0,'推荐用户')
			ws.write(num,1,'推荐用户归属地')
			ws.write(num,2,'省份')
			ws.write(num,3,'推荐时间')
			ws.write(num,4,'被推荐用户')
			ws.write(num,5,'被推荐用户归属地')
			ws.write(num,6,'省份')
			ws.write(num,7,'注册来源')
			ws.write(num,8,'注册时间')
			ws.write(num,9,'激活时间')
			for line in tmplist:
				num += 1
				lineArr = line.split(',')
				ws.write(num,0,lineArr[0])
				city1st = lineArr[1]
				prov1st = lineArr[2]

				if city1st == '2' or city1st == 'null':
					city1st = '未知'
					prov1st = '未知'
				ws.write(num,1,city1st)
				ws.write(num,2,prov1st)
				ws.write(num,3,lineArr[3])
				ws.write(num,4,lineArr[4])

				city2nd = lineArr[5]
				prov2nd = lineArr[6]
				if city2nd == '2' or city2nd == 'null':
					city2nd = '未知'
					prov2nd = '未知'
				ws.write(num,5,city2nd)
				ws.write(num,6,prov2nd)

				source = lineArr[7]
				if source == '\N':
					source = ''
				ws.write(num,7,source)
				ws.write(num,8,lineArr[8])
				ws.write(num,9,lineArr[9])
			
			start_index += page_size

		wb.save(targetFile)

if __name__ == '__main__':
	"""
	用法：python file_seg.py [源文件路径] [目标文件路径]
	源文件和目标文件路径都是必传的
	"""
	#0表示文件本身的路径，因此输入参数从1开始获取
	path = None
	targetPath = None
	try:
		path = sys.argv[1]
		targetPath = sys.argv[2]

		if path == None or not os.access(path,os.F_OK):
			raise Exception()
		if targetPath == None:
			raise Exception()
	except Exception, e:
		print '用法：python file_seg.py [源文件路径] [目标文件路径]'
		sys.exit(0)

	segFile = SegFile(path)
	segFile.writeToExcel(targetPath)
