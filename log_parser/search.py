#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:search.python
#统计每月的搜索次数
import os
import fnmatch

path = '/data/log/tomcat6'
regex = 'catalina.2013-0[45]*.log'
#flight_result = '/data/logs/hjb/flight.txt'
hotel_result = 'hotel_result.txt'
_files = []

try:
	for f in os.listdir(path):
		print 'match file %s' % f
		if fnmatch.fnmatch(f,regex):
			_files.append(f)
except Exception, e:
	print 'Error while list [%s] ,msg: %s' % (path,e)
finally:
	pass


if len(_files) > 0:
	for f in _files:
		print '>>> %s ' % f
		cmd = '''cat %s|grep "flightorder_url+flight+passengerinfo+cardinfo"|awk -F'telephone":"' '{print $2}'|awk -F'"' '{print $1}'|sort|uniq -c >>%s''' % (f,hotel_result)
		os.system(cmd)