#/usr/bin/env python
import httplib,urllib
import os

def get_event_content():
	#os.system('''export http_proxy=""''')
	_headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	_conn = httplib.HTTPConnection('172.16.80.110', int(9090))
	para = {'account':'15210078395','password':'5832638','account_type':1}
	data = urllib.urlencode(para)
	_conn.request('POST','/login.action',data,_headers)

	response = _conn.getresponse()
	if response.status == 200 and response.reason == 'OK':
		ret = response.read()

	print ret

if __name__ == '__main__':
	get_event_content()