#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from pymongo import Connection
from setting import db_conf
import inspect, functools


class Mongodb(object):
	'''数据库操作辅助类'''
	def __init__(self):
		self.db = None

	def conn(self):
		if not self.db:
			connection = Connection(db_conf['uri'])
			self.db = connection[db_conf['dbname']]
		return self.db

	def find_one(self, name):
		def wrapper(callback):
			def wrapper(*args, **kwargs):
				conn = self.conn()
				query = args[0]
				if '_id' in query:
					from bson.objectid import ObjectId
					if not isinstance(query['_id'], ObjectId):
						query['_id'] = ObjectId(query['_id'])
				return conn[name].find_one(query)
			return wrapper
		return wrapper

	def find(self, name,select=None, order=None, dump=False):
		def wrapper(callback):
			def wrapper(*args, **kwargs):
				conn = self.conn()
				query = args[0]
				cursor = conn[name].find(query, select)
				if 'limit' in kwargs: #limit
					cursor.limit(kwargs['limit'])
				if 'skip' in kwargs: #skip
					cursor.skip(kwargs['skip'])
				if order and isinstance(order, dict): #sort
					for k in order:
						cursor.sort(k, int(order[k]))
				# elif isinstance(order, tuple):
				# 	for k, v in p:
				# 		cursor.sort(k, int(v))	
				return [record for record in cursor] if dump or 'dump' in kwargs and kwargs['dump'] else cursor
			return wrapper
		return wrapper

	def save(self, name):
		def wrapper(callback):
			def wrapper(*args, **kwargs):
				conn = self.conn()
				obj = args[0]
				if not obj:
					raise ValueError("Not to be save null object")
				if 'addtime' not in obj:
					import datetime
					obj['addtime'] = datetime.datetime.now()
				if '_id' in obj:
					from bson.objectid import ObjectId
					if not isinstance(obj['_id'], ObjectId):
						obj['_id'] = ObjectId(obj['_id'])
				return conn[name].save(obj)
			return wrapper
		return wrapper

	def remove(self, name):
		def wrapper(callback):
			def wrapper(*args, **kwargs):
				conn = self.conn()
				query = args[0]
				if not query: return
				if '_id' in query:
					from bson.objectid import ObjectId
					if not isinstance(query['_id'], ObjectId):
						query['_id'] = ObjectId(query['_id'])
				return conn[name].remove(query,safe=True)['n']
			return wrapper
		return wrapper

# def make_mongodb_wrapper(name):
#     @functools.wraps(getattr(Mongodb, name))
#     def wrapper(*a, **ka):
#         return getattr(Mongodb(), name)(*a, **ka)
#     return wrapper

mongo = Mongodb()


