#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:client_reg_screen.py
import os
import sys
from datetime import datetime
import time

'''
截取推荐注册的用户中，从客户端注册的用户日志屏幕截图
'''
#当前程序的根目录
BASE = os.path.dirname(__file__)
#需要指定手机号码和日志文件名称
CMD_GREP = 'grep %s %s|grep register'
REG_LOG = 'client_reg.log'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
OUT_PATH = os.path.join(BASE,'client_out')

def getPicName(moInviter,moInvited):
	return '%s-%s-注册日志.png' % (moInviter,moInvited)

def loadClientRegs(fpath):
	'''从所有的注册日志中查找客户端注册的日志'''
	regList = open(fpath,'r').readlines()
	clientRegList = []
	for line in regList:
		#csv文件可能是tab键或者是逗号分隔
		arr = line.split(',')
		if len(arr) == 1:
			arr = line.split('\t')

		if arr[7] == '1':
			#print '客户端注册记录：%s' % line
			clientRegList.append(line)

	return clientRegList

def printScreen(regList):
	'''
	客户端的注册日志，需要判断用户的注册时间和激活时间的时间差。
	如果时间差在3秒以内，就不再截取这些用户的注册日志了。
	'''
	logPath = os.path.join(BASE,REG_LOG)
	for item in regList:
		os.system('clear')
		arr = item.split(',')
		if len(arr) == 1:
			arr = item.split('\t')

		#计算激活时间和注册时间的差值
		dtReg = datetime.strptime(arr[8],DATE_FORMAT)
		active = arr[9].replace('\r\n','')
		dtActive = datetime.strptime(active,DATE_FORMAT)
		diff = (dtActive - dtReg).seconds
		#如果激活时间和注册时间相差3秒以上，那么需要截取这个用户的注册日志
		if diff>3:
			cmd = CMD_GREP % (arr[4],logPath)
			print '======> %s ' % cmd
			os.system(cmd)
			time.sleep(1)
			screen(getPicName(arr[0],arr[4]))

#GTK截图
def screen(fname):
	import gtk.gdk
	w = gtk.gdk.get_default_root_window()
	sz = w.get_size()
	pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
	pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
	if (pb != None):
		pb.save("%s/%s.png" % (OUT_PATH,fname), "png")
	else:
		logging.error("Unable to get the screenshot for [%s]." % fname)

if __name__ == '__main__':
	fpath = os.path.join(BASE,'120new.csv')
	regs = loadClientRegs(fpath)
	printScreen(regs)

