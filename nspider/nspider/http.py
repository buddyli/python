#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import httplib, urllib

''''
    Http 工具类
'''
class Http:
    def __init__(self, host, port):
        self._host = host
        self._port = int(port)
        self._conn = None
        self._headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

    def request(self, data, host=None, port=None, headers=None):
        ret = None
        if self._conn is None:
            self._conn = httplib.HTTPConnection(host or self._host, port or self._port)
        self._conn.request("POST", "/umessage/service.do", data, headers or self._headers)
        response = self._conn.getresponse()
        if response.status == 200 and response.reason == "OK":
            ret = response.read()
        self._conn.close()
        return ret

if __name__ == '__main__':
    from configuration import config
    http = Http(config.getGlobal('host'), config.getGlobal('port'))
    print http.request('')