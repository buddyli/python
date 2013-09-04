#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from utils.hash import md5
import sys

if __name__ == '__main__':
    string = sys.argv[1]

    print 'str=', string
    print 'hash=', md5(string)