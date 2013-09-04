#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import os, logging, sys

#当前程序目录
BASE = os.path.dirname(__file__)
#日志文件路径
LOG_PATH = os.path.join(BASE, 'logs/%s.log' % (__file__,))
#创建日志文件目录
if not os.path.exists(os.path.dirname(LOG_PATH)):
    os.makedirs(os.path.dirname(LOG_PATH))
#日志格式
LOG_FORMAT = '%(asctime)s [%(levelname)s] : %(funcName)s,L%(lineno)d %(message)s'
#配置日志
logging.basicConfig(format=LOG_FORMAT, filename=LOG_PATH,level=logging.INFO)

data = os.path.join(BASE, 'gx.csv')

log_path = '/data/log_bk/wap'

#遍历目录
def search_dir(dirname):
    ret = []
    if os.path.isdir(dirname):
        for f in os.listdir(dirname):
            sub = os.path.join(dirname, f)
            if os.path.isdir(sub):
                ret.extend(search_dir(sub))
            else: ret.append(sub)
    else:
        ret.append(dirname)
    return ret


#搜索手机号日志
def search_mobile(logfile, mobile):
    import re
    for line in open(logfile, 'r'):#逐行匹配
        if re.search(mobile, line, re.DOTALL):
            print line
            gtk(name('12345','67890'))
            print 'OK'

#读取原始数据文件
def read():
    for line in open(data, 'r'):
        print line


#图片命名
def name(fno, lno):
    return '%s-%s.jpeg' % (fno, lno)


#QT截图
def qt4(fname):
    from PyQt4.QtGui import QPixmap, QApplication
    app = QApplication(sys.argv)
    QPixmap.grabWindow(QApplication.desktop().winId()).save('%s.png' % fname, 'png')
        
def gtk(fname):
    import gtk.gdk
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    if (pb != None):
        pb.save("%s.png" % fname, "png")
    else:
        logging.error("Unable to get the screenshot for [%s]." % fname)

def test():
    fs = search_dir(log_path)
    for f in fs:
        return search_mobile(f, '159')

#截图
def grab(fname):
    return gtk(fname)
    

if __name__ == '__main__':
    test()
