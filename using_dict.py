#!/usr/bin/python
#Filename:using_dict.py
#usage of dict

ab={'Swaroop':'swaroop@163.com',
	'licb':'dfdfdf@umessage.com.cn',
	'Mastunotot':'Mastunooo@umessage.com.cn',
	'Spammer':'Spammer@umessage.com.cn'
}
print "Swaroop's address is %s" %ab['Swaroop']

#Adding a key/value pair
ab['Guido']='guido@python.org'

#Deleting a key/value pair
del ab['Spammer']

print '\nThere are %d contacts in the address-book\n' %len(ab)
for name,address in ab.items():
	print 'Contact %s at %s' %(name,address)

if 'licb' in ab:#or ab.has_ke('licb')
	print "\nlicb's address is %s" %ab['licb']
