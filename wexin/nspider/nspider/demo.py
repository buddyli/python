#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from random import choice

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
    return '%s' % custom_choice(x,'abcdef012345679')


if __name__ == '__main__':
    print randomIMEI(30000)