#!/usr/bin/env python
# -*- coding:utf8 -*-

contacts = {
	'Alex':12345678,
	'Rachel':[123321,'student',25],
	'Rain':{'age':28},
}

#for i in contacts:#只打印key
#	print i 

#for i in contacts.items():打印出的是元祖
#	print i

contacts['Alex'] = 87654321#修改一个key对应的值

del contacts['Alex'] #删除一条

contacts['Alex Li'] = 87654321#添加一条

for k,v in contacts.items():#打印出key及对应的值
	print k,v


