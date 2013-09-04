#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import os, logging
import paramiko
from datetime import date

#当前程序目录
BASE = os.path.dirname(__file__)

#日志文件路径
LOG_PATH = os.path.join(BASE, 'logs/robot.%s.log' % (date.today().strftime('%Y%m%d')))

#创建日志文件目录
if not os.path.exists(os.path.dirname(LOG_PATH)):
    os.makedirs(os.path.dirname(LOG_PATH))

#日志格式
LOG_FORMAT = '%(asctime)s [%(levelname)s] : %(funcName)s,L%(lineno)d %(message)s'

#配置日志
logging.basicConfig(format=LOG_FORMAT, filename=LOG_PATH,level=logging.INFO)


CMD = "bzcat /data/logs/hjb/umserver.log.%s.bz2 | grep %s | grep invatation"


def remote_ssh(host, date, mobile):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host,22,'licb',key_filename='/home/licb/key/key_licb/id_rsa',timeout=5)
        print "==>%s" % (CMD % (date, mobile))
        stdin, stdout, stderr = ssh.exec_command(CMD % (date,mobile))

        for o in stdout.readlines():
            print o,
        ssh.close()
        try:
            save_screen(mobile)
        except :
            save_screen2(mobile)
    except Exception, ex:
        print '%s\tError\n%s'%(host, ex)


def save_screen2(mobile):
    import gtk.gdk
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    #pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    if (pb != None):
        pb.save("%s.png" % mobile,"png")
    else:
        print "Unable to get the screenshot."

#保存图片
def save_screen(mobile):
    import sys
    from PyQt4.QtGui import QPixmap, QApplication
    app = QApplication(sys.argv)
    QPixmap.grabWindow(QApplication.desktop().winId()).save('%s.png' % mobile, 'png')

if __name__ == '__main__':
    remote_ssh('172.16.80.220', '20130612','18378224924')        