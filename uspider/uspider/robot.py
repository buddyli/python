#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import uuid, os, json, httplib, threading, re, urllib, time, ConfigParser as CP

import logging, fnmatch

from pyDes import *
from threadpool import *
from random import choice
from struct import *
from gzip import GzipFile
from StringIO import StringIO
from datetime import date

#当前程序目录
BASE = os.path.dirname(__file__)

#配置文件目录
CONFIG_PATH = os.path.join(BASE, 'config')

#日志文件路径
LOG_PATH = os.path.join(BASE, 'logs/robot.%s.log' % (date.today().strftime('%Y%m%d')))

#创建日志文件目录
if not os.path.exists(os.path.dirname(LOG_PATH)):
    os.makedirs(os.path.dirname(LOG_PATH))

#日志格式
LOG_FORMAT = '%(asctime)s [%(levelname)s] : %(funcName)s,L%(lineno)d %(message)s'

#配置日志
logging.basicConfig(format=LOG_FORMAT, filename=LOG_PATH,level=logging.INFO)

logging  = logging.getLogger(__name__)

'''辅助函数'''
def package(password, data):
    binary = mb_encode(password, data)
    return '%s%s%s' % ("AA", password, gzip(binary))

# des 加密
def mb_encode(password, str):
    k = des(password, ECB, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    d = k.encrypt(str)
    return d

# des 解密
def mb_decode(password, strs):
    k = des(password, ECB, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    d = k.decrypt(strs, padmode=PAD_PKCS5)

# gzip 压缩
def gzip(data):
    io = StringIO()
    gz = GzipFile(fileobj=io, mode='wb')
    gz.write(data)
    gz.close()
    return io.getvalue()

# gzip 解压缩
def ungzip(data):
    io = StringIO(data)
    gz = GzipFile(fileobj=io, mode="rb")
    bytes = gz.read()
    gz.close()
    return bytes

# hex2int
def hex2int(hexstr):
    return int(re.sub('^0+','',hexstr),16)

# isGzip 
def is_gzip(data):
    return data[:2] == "\x1F\x8B" # GZIP头格式

# isZip
def is_zip(data):
    return data[:4] == "\x50\x4B\x03\x04" # zip头格式

# 打印回显数据
def print_result(request, data):
    if data[0:1] == '@':
        logging.info("**** Response #%s:%s" % (request.requestID, data[1:]))
    else:
        uuid = '%s' % data[:36] #请求的UUID
        size = hex2int(data[36:44]) # data length
        body = data[44:45+size] # 数据体
        if is_gzip(body): #按照协议，如果不是ZIP格式，那么必然是GZIP格式数据
            logging.info("**** Response #%s:%s" % (request.requestID, ungzip(body)))
        elif is_zip(body): #如果是 ZIP 格式文件
            logging.info("**** Response #%s:%s" % (request.requestID, "Revice zip data."))
        
# 处理异常信息
def handle_exception(request, exc_info):
        logging.error("**** Exception occured in request #%s: %s" % (request.requestID, exc_info))


##扫描配置文件
def scan_files(path):
    ret = []
    for fs in os.listdir(path):
        if fnmatch.fnmatch(fs, '*.ini'):
            ret.append(os.path.join(path, fs))        
    return ret

ac_conf = scan_files(os.path.join(CONFIG_PATH, 'action'))
dc_conf = scan_files(os.path.join(CONFIG_PATH, 'device'))

#拼装消息
def message():
    ac = choice(ac_conf)
    dc = choice(dc_conf)
    return actions(device(dc), action(ac))

# send Http Request
def send_request(count, echo = False):
    msg = message()
    conn = httplib.HTTPConnection("clientservice.12580.com", 9090) #hostname, port
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn.request("POST", "/umessage/service.do", msg, headers)
    response = conn.getresponse()
    if response.status == 200 and response.reason == "OK":
        return response.read() if echo else "@Reviced Data OK."
    else:
        raise RuntimeError("Http request exception:", response.status)

# 读取配置文件
def read_conf(path):
    configuration = CP.SafeConfigParser(allow_no_value=True)
    configuration.readfp(open(path, "rb"))
    return configuration

# create device
def device(configuration_path):
    data = {}
    config = read_conf(configuration_path)
    data['CP_CH'] = config.get("device","ch")
    data['CP_PRT'] = config.get("device","ptr")
    data['CP_UID'] = config.get("device","uid")
    data['CP_VER'] = config.get("device","ver")
    data['CP_TPL'] = config.get("device","tpl")
    data['CP_LON'] = config.get("device","lon")
    data['CP_LAT'] = config.get("device","lat")
    #data['CP_IMEI'] = '%s%s' % (imei(), config.get("device","imei")) #fb2b970a49b2c7b4eb0046746b
    data['CP_IMEI'] = '%s%s' % (imei(), 'fb2b970a49b2c7b4eb0046746b')
    data['CP_MODEL'] = config.get("device","model")
    data['CP_PLTFM'] = config.get("device","pltfm")
    data['CP_RATIO'] = config.get("device","ratio")
    data['CP_TOUCH'] = config.get("device","touch")
    data['CP_CITYID'] = config.get("device","cityid")
    data['CP_RESVER'] = config.get("device","resver")
    data['CP_PHONENUM'] = config.get("device","phonenum")
    data['CP_PUBRESPATH'] = config.get("device","pubrespath")
    return data

#create aciton
def action(configuration_path):
    data = {}
    config = read_conf(configuration_path)
    data['action'] = config.get("action","action")
    data['paras'] = dict(config.items('paras'))
    data['requuid'] = str(uuid.uuid1()) #请求使用的随机串
    return data

#create actions request
def actions(device,action):
    data = {}
    for p in device:
        data[p] = device[p]
    data['actions'] = []
    data['actions'].append(action)
    return package('password', json.dumps(data))


def custom_choice(count, strrange):
    strs = ''
    for i in xrange(count):
        strs += choice(strrange)
    return strs;

# create random IMEI
def imei():
    x = 5
    ret = '%s' % custom_choice(x,'0123456789abcdef')
    logging.info("**** random (%s)" % ret)
    return ret

    
#控制请求总数
def thread_count():
    return [x for x in xrange(MAX_REQUEST)]

MAX_REQUEST = 10

if __name__ == '__main__':
    requests = makeRequests(send_request, thread_count(), print_result, handle_exception)
    main = ThreadPool(20)
    for req in requests:
        main.putRequest(req)
        logging.debug("Work request #%s added." % req.requestID)
    while True:
        try:
            time.sleep(1)
            main.poll()
        except KeyboardInterrupt:
            SystemExit("Shutdown OK.")
            break;
        except NoResultsPending:
            SystemExit("Shutdown OK.")
            break;
    if main.dismissedWorkers:
        logging.debug("Joining all dismissed worker threads...")
        main.joinAllDismissedWorkers()
        










