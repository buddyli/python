#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from utils import *
from ftype import ftype
from configuration import config
from http import Http
from simulator import Mobile
import json, threading, time


class UmessageRequest(threading.Thread):
    def setEnv(self, config):
        self._config = config

    def doProcess(self, index, showInfo):
        try:
            mobile = Mobile()
            items = mobile.assemble(self._config.choiceDev(), int(self._config.getGlobal('count'))).__dict__
            items.update(self._config.choiceAct())
            data = package('password', json.dumps(items))
            http = Http(self._config.getGlobal('host'), self._config.getGlobal('port'))
            data = http.request(data)
            size = hex2int(data[36:44])
            body = data[44:45 + size]
            ret = None
            if showInfo:
                print 'start %s' % ("=" * 20)
                if ftype.isZIP(body):
                    ret = "BINARY"
                    print 'recv zip format data.'
                else:
                    ret = "TEXT"
                    print '%s' % ungzip(body)
                print 'End %s %s' % (index, "=" * 20)
            else: ret = body
        except:
            ret = None
        return ret

    def run(self):
        total = int(self._config.getGlobal('count'))
        sleep = int(self._config.getGlobal('sleep'))
        show = self._config.getGlobal('showDes')
        index = 0
        while index < total:
            index+=1
            if self.doProcess(index, show) is None:
                state = "Fail"
            else: state = "OK"
            print 'TOTAL:%s,CUR:%s, Process %s' % (total, index, state)
            time.sleep(sleep)

def assemble(count):
    mobile = Mobile()
    items = mobile.assemble(config.choiceDev(), count).__dict__
    items.update(config.choiceAct())
    return json.dumps(items)

def main():
    thread = UmessageRequest()
    thread.setEnv(config)
    thread.start()

if __name__ == '__main__':
    main()