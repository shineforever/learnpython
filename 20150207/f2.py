#!/usr/bin/env python
# -*- coding:utf8 -*-

with open ('f_test.txt','r+') as f:
	t = f.tell()
	print t
	print f.readline()
	print t
	f.seek(24)
	print t
	f.truncate(35)
	print t
