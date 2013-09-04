#!/usr/bin/env python
#-*- encoding:utf-8 -*-

'''文件类型判断'''

class FileType:
    ZIP_HEADER = "\x50\x4B\x03\x04" # zip头格式
    GZIP_HEADER = "\x1F\x8B" # GZIP头格式
            
    def isGZIP(self, data):
        return data[:2] == FileType.GZIP_HEADER

    def isZIP(self, data):
        return data[:4] == FileType.ZIP_HEADER

ftype = FileType()

if __name__ == '__main__':
    pass