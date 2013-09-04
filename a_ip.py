#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, re, logging, time
import urllib, socket, urllib2, urlparse
from urllib2 import URLError, Request, urlopen
from datetime import date

from threadpool import *

#当前程序目录
BASE = os.path.dirname(__file__)

#日志文件路径
LOG_PATH = os.path.join(BASE, 'logs/%s.%s.log' % ('ip' ,date.today().strftime('%Y%m%d')))

#创建日志文件目录
if not os.path.exists(os.path.dirname(LOG_PATH)):
    os.makedirs(os.path.dirname(LOG_PATH))

#日志格式
#LOG_FORMAT = '%(asctime)s [%(levelname)s] : %(funcName)s,L%(lineno)d %(message)s'
LOG_FORMAT = '%(message)s'


#配置日志
logging.basicConfig(format=LOG_FORMAT, filename=LOG_PATH,level=logging.INFO)


logging  = logging.getLogger(__name__)


#service = 'http://strategy.intra.umessage.com.cn:8180/WebDataHandler/phoneArea.search?theip=%s&at=4&vt=1&pt=1'
service = 'http://www.ip138.com/ips138.asp?ip=%s&action=2'

exp = r'''<td align="center"><ul class="ul1"><li>本站主数据：(?P<mdata>.*?)</li>'''
patten = re.compile(exp, re.DOTALL)

def send_request(ip):
    '''获取指定URL的内容'''
    try:
        url = service % ip.strip()
        socket.setdefaulttimeout(10)
        request = urllib2.Request(url)
        conn = urllib2.urlopen(request)
        data = conn.read()
        return data.decode('gbk', 'ignore').encode('utf-8')
    except Exception,ex:
        logging.error('<<< [%s] request fail.' % url)

# 打印回显数据
def print_result(request, data):
    #logging.info("**** Response #%s:%s" % (request.requestID, data))
    logging.info('%s,%s' % (data['ip'],data['name']))
        
# 处理异常信息
def handle_exception(request, exc_info):
    logging.error("**** Exception occured in request #%s: %s" % (request.requestID, exc_info))

def request(ip):
    data = send_request(ip)
    return parse_xml(data, ip)


def parse_xml(xml_data, ip):
    match = patten.search(xml_data)
    ret = {}
    ret['ip'] = ip.strip()
    ret['name'] = match.group('mdata') if match is not None else "Unknow"
    return ret




def parse_ips():
    return open('uniq.data', 'r').readlines()


THREAD_POOL_SIZE = 20

if __name__ == '__main__':
    requests = makeRequests(request, parse_ips(), print_result, handle_exception)
    main = ThreadPool(THREAD_POOL_SIZE)
    for req in requests:
        main.putRequest(req)
        logging.debug("Work request #%s added." % req.requestID)
    while True:
        try:
            time.sleep(1)
            main.poll()
        except KeyboardInterrupt:
            main.dismissWorkers(THREAD_POOL_SIZE, do_join=True)
            SystemExit("Shutdown OK.")
            break;
        except NoResultsPending:
            main.dismissWorkers(THREAD_POOL_SIZE, do_join=True)
            SystemExit("Shutdown OK.")
            break;
    if main.dismissedWorkers:
        logging.debug("Joining all dismissed worker threads...")
        main.joinAllDismissedWorkers()

