# -*- coding:utf-8 -*-
#!/usr/bin/python
#Filename:interface.py
#For:stastic interface useage during a period
import os
import time

#source dirs
#sources='/home/licb'
print 'Useage:you should input the dir path end with os.path!\
\nes:/home/licb/'
sources=raw_input('please input the absolute path of the source dir:')

#list all of the files except hidden ones
#the files you want  to list,names must be tuple but not list!!!
names=('umserver.log.201302','umserver.log.201303')
fileList=os.listdir(sources)

for name in fileList:
 if name.startswith('.'):
  continue  
 #elif name.startswith('umserver.log.201302') or name.startswith('umserver.log.201303'):
 elif name.startswith(names):
  print name
  cmd="cat %s%s|grep '>>>>,UUID'|awk -F'REQ_ACTION:' '{print $2}' | awk -F',' '{print $1}'" %(sources,name)
  if os.system(cmd) == 0:
   print 'process %s success' %name
  else:
   print 'process %s failure' %name
 else:
  #print name
  continue

#target dir
target_dir="/tmp/"


