#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:txt2excel.py
import os
import sys
import xlwt#用来写入excel表格的模块
import fnmatch
import re

reload(sys)
sys.setdefaultencoding('utf-8')

class Txt2Excel(object):
	"""txt文件转成excel"""
	def __init__(self):
		super(Txt2Excel, self).__init__()

	def convert(self):
		dir = "/home/licb/a/"
		regx = '[\d]{11}'
		pattern = re.compile(r'[\d]{11}')
		files = os.listdir(dir)
		#print files
		for f in files:
			flist = []
			ff = open(dir+f,'r')
			wb = xlwt.Workbook('utf-8')
			ws = wb.add_sheet('第一页')
			num = 0
			for line in ff:
				#print line
				if line == None or len(line) == 0:
					continue
				else:
					match = pattern.match(line)
					if match:
						ws.write(num,0,line)
						num += 1

			fname = f.split(".")[0]+".xls"
			print '保存到目标文件%s' % fname
			wb.save(fname)

if __name__ == '__main__':
	obj = Txt2Excel()
	obj.convert()