#!/usr/bin/python
# _*_ coding: UTF-8 _*_

from Channel import *
import sys
import time
#sys.path.append("..")

#以下只是测试数据，请使用者自行修改为可用数据
apiKey = "suQGf79FbjyvCg42Bg44qWsy"
secretKey = "dGr0lMX93E7kIruy6K5pNh1aifA1PLHY"
#user_id = "1578491886"
#channel_id = "3946349904645840715"

#message = "{'title':'baidu push','description':'message from python sdk'}"
#message = json.dumps(message)
#message_key = "key1"
#message_key = json.dumps(message_key)
#tagname = "test_tag"


def test_queryBindList():
	
	c = Channel(apiKey, secretKey)
	
	#optional = dict()
	
	#optional[Channel.CHANNEL_ID] =  channel_id
	
	c.queryBindList()	
	
	#print ret

if __name__ == '__main__': 
	
	test_queryBindList()


