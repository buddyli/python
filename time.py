#!/usr/bin/python
#times.py
#the params who have default value,should be put at the last
import time

def say(message,times=1):
	print message*times;

say('hello world');
say('hello world',5);
print time.strftime('%Y%m%d%H%M%S')
