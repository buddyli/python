#!/usr/bin/env python
#-*- encoding:utf-8 -*-

'''configuration tools'''

import os, fnmatch, uuid
import ConfigParser

from random import choice,random


class Configuration:
    def __init__(self, path=None):
        self.config = ConfigParser.SafeConfigParser(allow_no_value=True)
        self._path = path or os.path.dirname(os.path.abspath(__file__));
        self._actions = [] # []
        self._devices = [] # []
        self._settings = None # {}

    ##过滤配置文件
    def _filter(self,root):
        _files = []
        for _file in os.listdir(root):
            if fnmatch.fnmatch(_file, '*.ini'):
                _files.append(os.path.join(root, _file))
        return _files

    ##读取设备配置列表
    def _loadDev(self):
        _dir = self._filter(os.path.join(self._path, 'config/devices'))
        self._devices = [] #clear 
        for f in _dir:
            self.config.read(f)
            self._devices.append(dict(self.config.items('device')))

    ##读取请求参数列表
    def _loadAct(self):
        _dir = self._filter(os.path.join(self._path, 'config/actions'))
        conf = self.config
        self._actions = [] #clear
        for f in _dir:
            self.config.read(f)
            _act = {'action':conf.get('action', 'action'), 'paras':dict(conf.items('paras'))}
            self._actions.append(_act)

    ##读取基础配置信息
    def _loadSetting(self):
        self.config.read(os.path.join(self._path, 'config/setting.ini'))
        self._settings = dict(self.config.items('global'))

    ##加载所有的配置文件
    def reload(self):
        self._loadDev()
        self._loadAct()
        self._loadSetting()

    ##随机加载一个设备配置
    def choiceDev(self):
        if len(self._devices) == 0: self._loadDev()
        return choice(self._devices)

    ##随机加载一个请求参数
    def choiceAct(self):
        if len(self._actions) == 0: self._loadAct()
        ret = choice(self._actions)
        ret.update({'requuid':str(uuid.uuid1())})
        return {'actions': [ret]}

    ##加载全局配置
    def getGlobal(self, key):
        if self._settings is None: self._loadSetting()
        return self._settings.get(key) or None

config = Configuration()

if __name__ == '__main__':
    print config.choiceAct()
    print config.choiceDev()
    print config.getGlobal('count')