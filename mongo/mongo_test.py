#!/usr/bin/env python
#*-* encoding:utf-8 -*-
#Filename:mongo_test.py
import sys
from pymongo import MongoReplicaSetClient
from pymongo.collection import Collection

reload(sys)
sys.setdefaultencoding('utf-8')

class MongoTest(object):
	'''python连接mongo replicaset数据库测试'''
	hostPair = None
	repSet = None
	client = None
	def __init__(self,hostPair,repSet):
		'''hostPair:ReplicaSet的url,形式如'host1:port1,host2:port2';repSet复制集的ID'''
		self.hostPair = hostPair
		self.repSet = repSet

	def getClient(self):
		client = MongoReplicaSetClient(self.hostPair,replicaSet=self.repSet)
		return client

mongoTest = MongoTest('172.16.80.129:27010,172.16.80.129:27012,172.16.80.129:27014,172.16.80.129:27016','rs1')

if __name__ == '__main__':
	#生成一个MongoReplicaSetClient对象
	client = mongoTest.getClient()
	print client.primary
	print client.hosts

	#获取一个Database对象
	db = client.splat
	print db.collection_names()

	#获取一个Collection对象
	coll = Collection(db,'user_limit')
	#执行查询操作，获取一个Cursor对象，遍历Cursor就可以获取到想要的字段了。
	cursor = coll.find({"mobile":"15210078395"});
	print cursor.__getitem__(0)
	print cursor.__getitem__(0)['mobile']

		