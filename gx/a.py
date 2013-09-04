#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import re,os,urlparse

from datetime import date

import logging


#当前程序目录
BASE = os.path.dirname(__file__)

#日志文件路径
LOG_PATH = os.path.join(BASE, 'logs/%s.%s.log' % (__file__, date.today().strftime('%Y%m%d')))

#创建日志文件目录
if not os.path.exists(os.path.dirname(LOG_PATH)):
    os.makedirs(os.path.dirname(LOG_PATH))

#日志格式
#LOG_FORMAT = '%(asctime)s [%(levelname)s] : %(funcName)s,L%(lineno)d %(message)s'
LOG_FORMAT = '%(message)s'

#配置日志
logging.basicConfig(format=LOG_FORMAT, filename=LOG_PATH,level=logging.INFO)

regexp = r'''(?P<ip>.+) - - \[.+\] "GET (?P<query>/wapmember/.+?)\s+HTTP/1.0".+'''

pattern = re.compile(regexp, re.DOTALL)


regexp2 = r'''[+0-9]+'''

p2 = re.compile(regexp2, re.DOTALL)

mobile = []

#s = '''211.138.100.178 - - [11/Apr/2013:21:58:03 +0800] "GET /wapmember/register.do?account=A13959051Dg1&login_type=1&city_id=13010000&source=0&url=index%7C13010000%7C2ygpsylmml4&t=69649 HTTP/1.0" 200 3439'''

if __name__ == '__main__':
    for line in open('''wap_reg.log''', 'r').readlines():
        matcher = pattern.search(line)
        if matcher:
            ip = matcher.group('ip')
            q = matcher.group('query')
            p = urlparse.parse_qs(urlparse.urlparse(q).query)
            account = ''
            source = ''
            if 'account' in p:
                account = p['account'][0]
            if 'source' in p:
                source = p['source'][0]
            if account and account not in mobile and p2.search(account):
                mobile.append(account)
                logging.info("%s;%s;%s" % (account, ip, source))
                #print '''cache size:%s''' % len(mobile)








