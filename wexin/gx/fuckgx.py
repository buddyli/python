#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename:fuckgx.py
import os
import sys
import datetime
from sshServer import *
import Image,ImageFont,ImageDraw

reload(sys)
sys.setdefaultencoding('utf-8')

class FuckGx(object):
	"""提取这些号码的推荐明细，根据推荐记录是否注册、注册时间、注册来源等提取对应的日志"""
	fpath = None
	date_format = '%Y%m%d'
	fuckMobiles = ["18278365503","18378270477","15177206094","13737734299","13597327231","15295958921",
	"18278202484","18378234334","18378224924","14777225514","15977343630","14796210804","18290019532",
	"14796215974","18290019701","18290020765","18378239334","13481373652","18290068079","14796219714",
	"15224647004","13481373652","15977342499","13617732655","14796210804","13481373848","18290020955",
	"18378270863","15077258748","15977284724","15977252451","18277305043","13597278704","18778235144",
	"18277304003","13471274619","18290023973","13471274739","18277304901","18290046268","15296809814",
	"18290023970","18278522321","13471255487","13471255473","18277305354","18290026882","18378290624",
	"15977343630","18290024535","13481373652","13737734299","13617732655","14796210804","18378224924",
	"18290013570","15977252451","18290026170","18290028977","18778238204","18278527917","18269535334",
	"18276557341","15296809814","18278529751","18276550677","18378295484","18378295064","18276554625",
	"18276554636","18378234334","18378299404","18290068202","18269530944","18269535542","13687827524",
	"18776468320","18278527006","13597330767","18377202802","18290062073","13597330793","18269535745",
	"18278529353","18269546546","18776510197","15977284724","18269556899","18776510353","18378544763",
	"15977343028","14796213104","18278520582","18377200484","18278521765","18269535480","18776468900",
	"18775099364","18378257934","18775099614","13977102871","15878248494","18269555856","18269557109",
	"18378255504","18276551467","18276554059","13768560864","18276553746","14796251977","18269554119",
	"18775099416","18378258404","18378270706","18378543954","18776469019","18278525261","18276966141",
	"18276552559"]
	def __init__(self,fpath):
		super(FuckGx, self).__init__()
		#启动时初始化本列表
		#self.flist = self.loadToList()
		self.fpath = fpath

	def getInviteByMobile(self,mobile):
		flist = []
		cmd = 'grep %s %s >tmp.txt' % (mobile,self.fpath)
		os.system(cmd)
		f = open('tmp.txt','r')
		for line in f:
			flist.append(line)

		f.close()
		return flist

	def loadToList(self):
		"""加载目标文件到list中"""
		flist = []
		f = open(self.fpath,'r')
		for line in f:
			flist.append(line)

		f.close()
		#print len(flist)
		return flist

	def getInviteLog(self,inviteList):
		'''统计一下该用户都在几号推荐过'''
		inviteDateDict = {}
		for invite in inviteList:
			rArr = invite.split(',')[3].split(' ')
			inviteDateDict[rArr[0]] = rArr[0]
		#print inviteDateDict
		return inviteDateDict

	def printInviteLog(self,dateDict,mobile):
		#for (k,v) in dateDict.items():
		#	print '' % (k,v)
		sshServer = GXScreenShot()
		ssh = sshServer.login_by_pubkey('172.16.80.220',22,'licb','/home/licb/key/key_licb/id_rsa')
		num = 1
		fList = []
		for i in dateDict:
			value = dateDict[i]
			fname = 'umserver.log.%s.bz2' % (value.replace('-',''))
			cmd = 'bzcat /data/logs/hjb/%s|grep %s|grep invatation' % (fname,mobile)
			print '%s' % (cmd)
			resultF = '%s-邀请好友推荐日志%d.txt' % (mobile,num)
			sshServer.getLogBySSH(ssh,cmd,resultF)
			num += 1
			fList.append(resultF)

		sshServer.closeSSH(ssh)
		return fList

	def txt2Image(self,fileList):
		for f in fileList:
			print '转换%s为图片...' % f
			rf = open(f,'r')
			text = ''
			for line in rf:
				text += line
			
			print text
			im = Image.new("RGB", (300, 50), (255, 255, 255))
			dr = ImageDraw.Draw(im)
			font = ImageFont.truetype('/usr/share/fonts/wps-office/FZCCHK.TTF', 18)
			dr.text((10, 5), text, font=font, fill="#000000")
			im.show()
			index = f.find('.',0)
			im.save(f[0:index]+".png")

if __name__ == '__main__':
	fgx = FuckGx('/home/licb/python/gx/fuckgx_new.csv')
	flist = fgx.getInviteByMobile('18278365503')
	print flist[2]
	dict = fgx.getInviteLog(flist)
	list2 = fgx.printInviteLog(dict,'18278365503')
	fgx.txt2Image(list2)