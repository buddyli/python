#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import Image,ImageDraw,ImageFont
import os

def txt2Image(fileList):
	for f in fileList:
		print '转换%s为图片...' % f

		index = f.find('.',0)
		java_cmd = '/usr/bin/env java -cp jar/commons-io-2.1.jar:jar/img.jar com.umessage.datareport.util.CeateCheckPic %s' % f
		os.system(java_cmd)

if __name__ == '__main__':
	fileList = ['/home/licb/python/gx/18278365503-邀请好友推荐日志1.txt',
	'/home/licb/python/gx/18278365503-邀请好友推荐日志2.txt',
	'/home/licb/python/gx/18278365503-邀请好友推荐日志3.txt']
	txt2Image(fileList)