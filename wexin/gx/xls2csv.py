#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:xls2csv.py

import os
import sys
from base import from_this_dir
import xlrd

reload(sys)
sys.setdefaultencoding('utf-8')

class Xls2Csv(object):
	"""广西活动期间的推荐数据太多，转换成csv格式处理"""
	csv = []
	def __init__(self):
		super(Xls2Csv, self).__init__()

	def getWorkBook(self,fname):
		#可以将formatting_info参数设置为false试试
		self.book = xlrd.open_workbook(from_this_dir(fname), formatting_info=True)

	def convert(self):
		snum = self.book.nsheets
		print '表格共有[%d]个sheet页' % snum
		for index in range(snum):
			#sheetName = '第%d页' % index
			#也可以直接按照sheet页面的下标访问
			#sheet_by_index(sheetx)
			sheet = self.book.sheet_by_index(index)
			#每个sheet的第一行是标题，不用处理
			for row in range(sheet.nrows):
				line = ''
				if row == 0:
					continue
				for col in range(14):
					cell = sheet.cell(row,col)
					if col == 0:
						line += str(cell.value)
					else:
						line += ','+ str(cell.value)

				line += '\n'
				print line
				self.csv.append(line)

		result = os.path.join(os.path.dirname(os.path.abspath(__file__)),'gx88w.csv')
		print '输出结果到 %s' % result
		open(result,'w').writelines(self.csv)


obj = Xls2Csv()
obj.getWorkBook('gx_2013-08-14 17:20:04.xls')
obj.convert()