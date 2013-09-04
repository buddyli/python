#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import os, sys

import logging,time
from datetime import date

"""获取WAP用户注册日志屏幕截图"""

#当前程序目录
BASE = os.path.dirname(__file__)
#日志文件路径
LOG_PATH = os.path.join(BASE, 'logs/%s.log' % (__file__,))
#创建日志文件目录
if not os.path.exists(os.path.dirname(LOG_PATH)):
    os.makedirs(os.path.dirname(LOG_PATH))

OUT_PATH = os.path.join(BASE, 'wap_reg_out')

if not os.path.exists(OUT_PATH):
    os.makedirs(OUT_PATH)    
#日志格式
LOG_FORMAT = '%(message)s'
#配置日志
logging.basicConfig(format=LOG_FORMAT, filename=LOG_PATH,level=logging.DEBUG)

data = os.path.join(BASE, 'gx2reg.txt')


log_path = '/home/licb/log/wap'

#预处理手机号日志，获取推荐手机号，被推荐手机号，和被推荐手机号的注册日期
def pre_process_log():
    import re
    #18276553746,13707816616,2013-06-27
    ret = []
    for line in open(data, 'r'):
        ret.append(re.search('(?P<fno>.+),(?P<lno>.+?),(?P<time>.+?)\s', line, re.M))
    return ret
    
#生成图片的文件名        
def image_name(m):
    return '%s-%s-注册日志' % (m.group('fno'), m.group('lno'))

server = ['23','24','124','125']

#计算当前手机号注册所在的日志
def guess_log(m):
    import datetime
    fdate = m.group('time')
    if fdate == None or fdate == '\N':
        return []
        
    theday = datetime.date(*map(int, fdate.split('-')))
    prevday = theday - datetime.timedelta(days=1)
    ret = []
    for svr in server:
        f1 = '%s/%s/tomcat_access_log.%s' % (log_path, svr, theday.strftime('%Y%m%d'))
        f2 = '%s/%s/tomcat_access_log.%s' % (log_path, svr, prevday.strftime('%Y%m%d'))
        if os.path.exists(f1):
            ret.append(f1)
        if os.path.exists(f2):
            ret.append(f2)
    return ret

#搜索手机号日志
# def search_mobile(m):
#     clear_screen() #清屏
#     import re
#     lno = m.group('lno')
#     logs = guess_log(m) #四台机器日志，每台查找两天，总共是8份日志
#     for log in logs:
#         print u'''在%s中查找%s的注册日志''' %(log, lno)
#         for line in open(log, 'r'):#逐行匹配
#             if re.search(lno, line, re.DOTALL):
#                 print line #打印日志

#     gtk(image_name(m))
#     return 'found %s finish.' % lno


cmd = "/bin/grep register  %s | /bin/grep %s"

#搜索手机号日志
def search_mobile(m):
    clear_screen() #清屏
    import re
    lno = m.group('lno')
    logs = guess_log(m) #四台机器日志，每台查找两天，总共是8份日志
    for log in logs:
        fcmd = cmd % (log, lno)
        print fcmd
        os.system(fcmd)                
    gtk(image_name(m))


#调用系统清屏命令
def clear_screen():
    os.system('clear')

#GTK截图
def gtk(fname):
    import gtk.gdk
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    if (pb != None):
        pb.save("%s/%s.png" % (OUT_PATH,fname), "png")
    else:
        logging.error("Unable to get the screenshot for [%s]." % fname)
            

def main():
    ms = pre_process_log()
    for m in ms:
        search_mobile(m)   
    

if __name__ == '__main__':
   main()
