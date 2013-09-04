#!/usr/bin/python
#filename:using_list.py

#def a shopping list
shoplist=['appale','mango','carrot','banana','orange'];

print 'I have',len(shoplist),'items to purchase';

#print those content into oneline
print 'These items are:',
#notice:there is a ":" at the end of  the line
for item in shoplist:
	print item,

print '\nI also have to buy rice.'
shoplist.append('rice')
print 'My shopping list is now',shoplist;

print 'sort the shop list'
shoplist.sort();
print 'Sorted shopping list is:',shoplist

print 'The first item i will buy is',shoplist[0]
olditem=shoplist[0]
del shoplist[0]
print 'I bought the',olditem
print 'My shopping list is now',shoplist
