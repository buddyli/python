#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:client_invite_screen.py
import os
import sys
from datetime import datetime
import time

"""
从客户端邀请日志中截取每个号码每日的推荐日志
输入文件：client_invite.log，客户端邀请日志，文件内容不变。
		第31行输入文件为用户的推荐记录元文件，格式为“推荐号码，推荐日期（yyyy-MM-dd）”
输出：输出到与当前文件同一个目录下的client_invite_out目录中
"""
#当前程序的根目录
BASE = os.path.dirname(__file__)
#需要指定手机号码。文件名称、推荐日期
CMD_GREP = 'grep %s %s|grep %s'
#活动期间客户端的邀请日志，这个内容不会变
REG_LOG = 'client_invite.log'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
OUT_PATH = os.path.join(BASE,'client_invite_out')

if not os.path.exists(OUT_PATH):
	os.makedirs(OUT_PATH)

def getPicName(mobile,date):
	return '%s推荐日志%s.png' % (mobile,date)

def printScreen(fpath):
	logPath = os.path.join(BASE,REG_LOG)
	sourcePath = os.path.join(BASE,fpath)
	inviteList = open(sourcePath,'r').readlines()
	for item in inviteList:
		os.system('clear')
		arr = item.split(',')
		cmd = CMD_GREP % (arr[0],logPath,arr[1])
		print '======> %s ' % cmd
		os.system(cmd)
		#这里的线程休眠是以秒为单位的，需要注意
		time.sleep(1)
		timeStr = arr[1].replace('-','')
		timeStr = timeStr.replace('\r','')
		timeStr = timeStr.replace('\n','')
		timeStr = timeStr.replace(' ','')
		#print timeStr
		screen(getPicName(arr[0],timeStr))

#GTK截图
def screen(fname):
	import gtk.gdk
	w = gtk.gdk.get_default_root_window()
	sz = w.get_size()
	pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
	pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
	if (pb != None):
		pb.save("%s/%s" % (OUT_PATH,fname), "png")
	else:
		logging.error("Unable to get the screenshot for [%s]." % fname)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print 'python client_invite_screen [目标文件]'
		sys.exit(0)

	fpath = sys.argv[1]
	if fpath == None or not os.access(fpath,os.F_OK):
		print '请输入正确的目标文件路径。。。'
		sys.exit(0)
	
	printScreen(fpath)

