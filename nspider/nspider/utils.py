#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from pyDes import *
from gzip import GzipFile
from StringIO import StringIO

import re

'''辅助函数'''
# des 加密
def mb_encode(password, str):
    k = des(password, ECB, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    d = k.encrypt(str)
    return d

# des 解密
def mb_decode(password, strs):
    k = des(password, ECB, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    d = k.decrypt(strs, padmode=PAD_PKCS5)
    return d

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
def hex2int(hexStr):
    return int(re.sub('^0+','',hexStr),16)

# 对数据进行包装
def package(password, data):
    binary = mb_encode(password, data)
    return '%s%s%s' % ("AA", password, gzip(binary))