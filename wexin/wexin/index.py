#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from bottle import route, request, response, default_app
from xml.dom.minidom import parseString
from datetime import datetime
import xml.etree.ElementTree as ET
import hashlib, time, re

token = 'token';

'''
    验证站点有效性
'''
@route('/', method='GET')
def default():
    args = []
    signature = request.GET.get('signature')
    args.append(request.GET.get('timestamp') or "")
    args.append(request.GET.get('nonce') or "")
    args.append(token)
    echostr = request.GET.get('echostr')
    args.sort()
    strs = hashlib.sha1(''.join(args)).hexdigest()
    return echostr if strs == signature else 'error'


message_tpl = u'''
<xml>
 <ToUserName><![CDATA[%s]]></ToUserName>
 <FromUserName><![CDATA[%s]]></FromUserName>
 <CreateTime>%s</CreateTime>
 <MsgType><![CDATA[text]]></MsgType>
 <Content><![CDATA[%s]]></Content>
 <FuncFlag>0</FuncFlag>
 </xml>
 '''

'''
<xml><ToUserName><![CDATA[gh_efe2ceb54bfe]]></ToUserName>
<FromUserName><![CDATA[oHfn2jrzCcUAlJlJY7h88nbkwWuk]]></FromUserName>
<CreateTime>1362725546</CreateTime>
<MsgType><![CDATA[location]]></MsgType>
<Location_X>39.860196</Location_X>
<Location_Y>116.387371</Location_Y>
<Scale>15</Scale>
<Label><![CDATA[中国北京市丰台区马家堡东路36号 邮政编码: 100000]]></Label>
<MsgId>5852861653493743795</MsgId>
</xml>
'''


@route('/', method='POST')
def process():
    for key, value in request.POST.allitems():
        print '%s==%s' % (key, value)
        msg = parse_msg(key)
        _type = msg['MsgType']
        _to = msg['ToUserName']
        _from = msg['FromUserName']
        if _type == 'location': #location message
            _cmd = 'location'
        elif _type == 'image': #text message
            _cmd = 'image'
        else:
            _cmd = msg['Content']
    
    if _cmd == "Hello2BizUser":
        message = "欢迎，欢迎，热烈欢迎。"
    elif _cmd == "location":
        if msg['Location_X'] and msg['Location_Y']:
            message = "您的坐标是LON:%s,LAT:%s" % (msg['Location_X'], msg['Location_Y'])
        if msg['Label']:
            message += "您的位置是:%s" % msg['Label']
        message += ",您想在附近约pao吗?"
    else:
        if re.match(u'[是,Y,y,想,好]', _cmd) is not None:
            message = "想好事呢吧。哈哈..."
        else:
            message = "现在时间是:%s" % datetime.now()



    strs = message_tpl % (_from, _to, int(time.time()), message)
    print strs
    return strs

def parse_msg(rawmsgstr):
    root = ET.fromstring(rawmsgstr)
    msg = {}
    for child in root:
        msg[child.tag] = child.text
    return msg

if __name__ == '__main__':
    default()
else:
    application = default_app()
