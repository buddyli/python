#!/usr/bin/evn python
#*-* encoding:utf-8 -*-
#Filename:rename.py
#为了批量重命名android的渠道包开发的。目前仅仅适用Android平台

import os
import sys
from ftplib import FTP
#import copy_apk

#设置一下字符编码
reload(sys)
sys.setdefaultencoding('utf-8')

#几个常用的常熟
ftp_host = '172.16.18.249'
ftp_user = 'view'#ftp用户名
ftp_passwd = 'umessage'#ftp密码
ftp_dir = '渠道发布包/'#渠道包在ftp服务器的根目录
android_dir = 'Android/'#Andriod渠道包的相对目录
ios_dir = 'IOS/'#ios渠道包的相对目录
wp_dir = 'Windows Phone/'#WP渠道包的相对目录

#文件保存的目录，版本号：格式为"2_6_3"等
def rename(dir,ver,plat = 'android'):
	'''dir:安装包保存的本地目录;ver:字符串形式的安装包版本号，用来重命名安装包'''
	fs = os.listdir(dir);
	for f in fs:
		arr = f.split('.')
		pkg_name = arr[3]
		channel = pkg_name[2:6]
		new_name = '12580_%s_%s_%s.apk' % (plat,ver,channel)
		cmd = 'mv %s %s' % (f,new_name)
		#print cmd
		os.chdir(dir)
		os.system(cmd)

#登录ftp服务器，拉取符合条件的文件值本地目录
#注意行参的声名，有默认值的参数必须放到后面
def pag_from_ftp(local_dir,server_dir = ftp_dir):
	#登录
	ftp = FTP(ftp_host)
	ftp.set_debuglevel(2)#打开调试级别日志
	ftp.login(ftp_user,ftp_passwd)
	
	#切换到工作目录下
	print '>>>> get files from dir: %s' % server_dir
	ftp.cwd(server_dir)

	#下载该目录下的文件
	f_list = ftp.nlst()
	if len(f_list) > 0:
		os.chdir(local_dir)
		print 'change to local store dir %s' % local_dir

		for f in f_list:
			print 'down file %s from ftp server' % f

			#fpath = '%s%s' % (server_dir,f)
			f_local = open(os.path.basename(f),'wb')
			ftp.retrbinary('RETR %s' % f,f_local.write)#获得一个文件操作句柄，当作第二个参数
			f_local.close()

	#最后不要忘了关闭已经打开的链接
	ftp.close()

web_dir = '/usr/local/umclient/Data/upfile_www/'
wap_dir = '/usr/local/umclient/Data/upfile_wap/'
#将文件拷贝到web和wap下载站点的工作目录
def copy_pkg(local_dir,webdir = web_dir,wapdir = wap_dir):
	print '安装包源目录[%s],拷贝目标目录[%s,%s]' % (local_dir,webdir,wapdir)
	cp_web = 'cp %s/* %s' % (local_dir,webdir)
	cp_wap = 'cp %s/* %s' % (local_dir,wapdir)

	os.system(cp_web)
	os.system(cp_wap)

if __name__ == '__main__':
	#发布标记，默认是关的
	release = 'n'
	if len(sys.argv) < 2:
		print 'USEAGE:python down_apk_from_ftp.py 版本号[2.6.4] [发布标记[y/n]]'
		sys.exit(0)
	else:
		ver = sys.argv[1]
		if len(sys.argv) >= 3:
			release = sys.argv[2]

	#BASE = os.path.dirname('/tmp')
	tmp_apk_dir = os.path.join('/tmp','apk')
	if os.path.exists(tmp_apk_dir):
		print '====清空安装包本地保存目录 %s' % tmp_apk_dir
		for f in os.listdir(tmp_apk_dir):
			fpath = os.path.join(tmp_apk_dir,f)
			print '===删除已经存在的apk安装包 %s' % fpath
			os.remove(fpath)
	else:
		print '====安装包本地保存目录 %s 不存在，创建之====' % tmp_apk_dir
		os.makedirs(tmp_apk_dir)
	#下载所有渠道的Android安装包
	pag_from_ftp(tmp_apk_dir,'渠道发布包/Android/%s/' % ver)
	pag_from_ftp(tmp_apk_dir,'正式发布包/Android/%s/' % ver)
	ver = ver.replace('.', '_')
	rename(tmp_apk_dir,ver)

	#如果用户选择了直接发布安装包，那么将安装包同步到发布目录下
	print '>>>>>>>>>>>>> %s' % release
	if release == 'y' or release == 'Y':
		print '=====发布安装包======'
		copy_pkg(tmp_apk_dir)
		#web_dir = '/home/licb/wap/'
		#wap_dir = '/home/licb/web/'
		#copy_pkg(tmp_apk_dir,web_dir,wap_dir)
