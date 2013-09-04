#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:evidence_screenshot.py
import os
import sys
import paramiko
import datetime

class GXScreenShot(object):
	"""
	广西推荐有奖活动日志截屏
	推荐日志：登录80.220根据推荐日期截取推荐日志
	注册日志：登录80.23,80.24,80.124,80.125根据注册日期和来源提取注册日志

	如果注册来源为1，先判断号码的注册时间和激活时间，如果相差很近，就不再截取注册和激活截图；
		否则，登录80.220截取这些用户注册和激活截图
	"""
	def __init__(self):
		super(GXScreenShot, self).__init__()

	#使用public key的登录服务器，执行指定的命令，输入到目标文件中
	def login_by_pubkey(self,serverHost,serverPort,userName,keyFile):
		known_host = "/home/licb/.ssh/known_hosts"
		ssh = paramiko.SSHClient()
		ssh.load_system_host_keys(known_host)
		#设置默认接收主机信任的策略，但是可能报告“不信任主机的”异常
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		print 'Connectting host %s......' % serverHost
		ssh.connect(serverHost,serverPort,username = userName,key_filename = keyFile)
		print 'Connect host %s sucess' % serverHost

		return ssh
		
	def getLogBySSH(self,ssh,cmd,fname):
		'''在服务器执行对应操作，并且记录服务器日志'''
		stdin,stdout,stderr = ssh.exec_command(cmd)
		f = file(fname,'w')
		for line in stdout.readlines():
			print line
			f.write(line)

		f.close()

	def closeSSH(self,ssh):
		ssh.close()

	def printScreen(self):
		res = open('5invite.txt','r').readlines()
		ssh = self.login_by_pubkey('172.16.80.220',22,'licb','/home/licb/key/key_licb/id_rsa')
		CMD = "bzcat /data/logs/hjb/umserver.log.%s.bz2 | grep %s | grep invatation"
		for line in res:
			mo = line.split(',')[0]
			time = line.split(',')[1]
			time = time.replace('-','')
			time = time.replace('\n','')
			print '==>%s' % (CMD % (time,mo))

			stdin, stdout, stderr = ssh.exec_command(CMD % (time,mo))
			for o in stdout.readlines():
				print o,
			pname = '%s推荐日志%s.png' % (mo,time)
			print pname
			try:
				self.save_screen(pname)
			except :
				self.save_screen2(pname)

		self.closeSSH(ssh)

	def save_screen2(self,pname):
	    import gtk.gdk
	    w = gtk.gdk.get_default_root_window()
	    sz = w.get_size()
	    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
	    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
	    if (pb != None):
	        pb.save(pname,"png")
	    else:
	        print "Unable to get the screenshot."

	#保存图片
	def save_screen(self,pname):
	    import sys
	    from PyQt4.QtGui import QPixmap, QApplication
	    app = QApplication(sys.argv)
	    QPixmap.grabWindow(QApplication.desktop().winId()).save(pname, 'png')

if __name__ == '__main__':
	#ips = ['172.16.80.110,22,licb,/home/licb/key/key_licb/id_rsa',
	#'172.16.80.111,22,licb,/home/licb/key/key_licb/id_rsa',
	#'172.16.80.130,22,umclient,/home/licb/key/id_rsa',
	#'172.16.80.131,22,umclient,/home/licb/key/id_rsa',
	#'172.16.80.23,22,guoxq,/home/licb/key/wap/wangm',
	#'172.16.80.24,22,guoxq,/home/licb/key/wap/wangm',
	#'172.16.80.124,22,guoxq,/home/licb/key/wap/wangm',
	#'172.16.80.125,22,guoxq,/home/licb/key/wap/wangm',
	#'172.16.101.242,22,guoxq,/home/licb/key/wap/wangm',
	#'172.16.101.243,22,guoxq,/home/licb/key/wap/wangm']
	screenShot = GXScreenShot()
	screenShot.printScreen()
