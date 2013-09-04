#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:screenInvite.py
import os
import sys

def loadInvite():
	invites = open('gxinvite.log',r).readlines()

cmd = 'grep %s gxinvite.log|grep %s|grep invatation'
def getInvite(mobile,date):
	print os.system(cmd % (mobile,date))

gxlist = open('5invite.txt','r').readlines()
for line in gxlist:
	mo = line.split(',')[0]
	date = line.split(',')[1]
	getInvite(mo,date)

