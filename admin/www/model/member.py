#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from misc import *

from misc.mongo import mongo as m

class MemberModel(object):
	'''基础数据模型'''

	@m.find_one(name="members")
	def find_one(self, *args, **kwargs): pass

	@m.save(name="members")
	def save(self, *args, **kwargs): pass

	@m.remove(name="members")
	def remove(self, *args, **kwargs): pass

	@m.find(name="members", select={'_id':1}, order={'_id':-1}, dump=True)
	def find(self, query, limit=None, skip=None): pass

	@m.find(name="members")
	def find_3(self, query): pass

if __name__ == '__main__':
	model = MemberModel()
	#print model.save({'password':'51db05d3421aa9042bad21bc','username':'test user'})
	#print model.save({'password':'51db05d3421aa9042bad21bc','username':'test user'})
	#print model.save({'password':'51db05d3421aa9042bad21bc','username':'test user'})
	print model.find({'password':'51db05d3421aa9042bad21bc','username':'test user'}, limit=2,skip=0)
	print model.find_3({'password':'51db05d3421aa9042bad21bc','username':'test user'})
	#print model.find_one({'password':'51db05d3421aa9042bad21bc','username':'test user'})
	#print model.remove({'password':'51db05d3421aa9042bad21bc','username':'test user'})
	#print model.find({'password':'51db05d3421aa9042bad21bc','username':'test user'},dump=True)
