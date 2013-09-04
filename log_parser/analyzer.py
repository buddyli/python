#!/usr/bin/env python
#-*- encoding:utf-8 -*-


import os,fnmatch


valid = ['couponslist','gettrainlistbystation','gettraininfo',
'station_by_address','getbusbyline',
'getbusbysestation','getbusbystation','getbusdetail','search',
'searchandrange','searchbranchandrange','searchbybranch',
'searchbydistancerange','searchbymerchant','getweather','merchantdetail','gettrainlistbyid']


log_dir = None ##日志目录
format = ".bz2" ##日志后缀名


def scan_dir(path):
    files = []
    for file in os.listdir(path):
        if fnmatch.fnmatch(file, format):
            files.append(file)
    return files

def readBzip(file):
    pass

if __name__ == '__main__':
    print scan_dir('./')