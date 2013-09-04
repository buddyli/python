#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import urllib, socket, urllib2, urlparse
from urllib2 import URLError, Request, urlopen
import multiprocessing as mp




def sendRequest(url):
    socket.setdefaulttimeout(10)
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
    request.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    request.add_header('Accept-Encoding','gzip, deflate')
    request.add_header('Accept-Language','zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3')
    conn = urllib2.urlopen(request)
    return {'url': url, 'response': conn.read()}


class RequestPool(object):
    def __init__(self, urls):
        self.urls = urls
        self.result = []

    def callback(self, data):
        self.result.append(data)

    def send(self):
        pool = mp.Pool()
        for url in self.urls:
            pool.apply_async(sendRequest,args=(url,), callback=self.callback)
        pool.close()
        pool.join()
        return self.result

if __name__ == '__main__':

    req = RequestPool((u'http://www.baidu.com/',u'http://www.google.cn/',))
    print req.send()