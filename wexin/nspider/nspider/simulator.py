#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import json
from random import choice,random

class Mobile:
    """ 手机基础属性 """

    def __init__(self):
        self.CP_CH = None  #渠道
        self.CP_CITYID = None #城市ID
        self.CP_IMEI = None #串号
        self.CP_MODEL = None #手机型号
        self.CP_PLTFM = None #手机平台
        self.CP_PRT = None #手机产品号 !important
        self.CP_RATIO = None #手机分辨率
        self.CP_TOUCH = None #是否触摸屏
        self.CP_UID = None #用户ID--登陆用户标示
        self.CP_VER = None #平台版本 
        self.CP_PHONENUM = None #手机号
        self.CP_TPL = None #手机适配模板类型
        self.CP_RESVER = None #资源版本号
        self.CP_PUBRESPATH = None #公共资源路径- cache路径
        self.CP_LON = None #手机经
        self.CP_LAT = None #手机维度

    #装配手机参数
    def assemble(self, config, count=None):
        self.CP_CH = config["ch"]
        self.CP_CITYID = config["cityid"]
        self.CP_IMEI = '%s%s' % (randomIMEI(count or 10000), config["imei"])
        self.CP_MODEL = config["model"]
        self.CP_PLTFM = config["pltfm"]
        self.CP_PRT = config["ptr"]
        self.CP_RATIO = config["ratio"]
        self.CP_TOUCH = config["touch"]
        self.CP_UID = config["uid"]
        self.CP_VER = config["ver"]
        self.CP_PHONENUM = config["phonenum"]
        self.CP_TPL = config["tpl"]
        self.CP_RESVER = config["resver"]
        self.CP_PUBRESPATH = config["pubrespath"]
        self.CP_LON = config["lon"]
        self.CP_LAT = config["lat"]
        return self

    def __str__(self):
        return '%s' % self.CP_IMEI

def custom_choice(count, strrange):
    strs = ''
    for i in xrange(count):
        strs += choice(strrange)
    return strs;

#生成随机数
def randomIMEI(count):
    x = 2
    if count >= 40000:
        x = 5
    elif count >= 30000:
        x = 4
    elif count >= 20000:
        x = 3
    return '%s' % custom_choice(x,'ab012345679')
