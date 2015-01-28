#!/usr/bin/env python
#-*- coding:utf8 -*-

import os
import readline
 
account_file = 'account.txt'
lock_file = 'lock.txt'


for i in range(3):
	username = raw_input('username:').strip()
	ff = file(lock_file)
	isLock = False
	for line in ff.readlines():
		if username == line.split()[0]:
			print 'Your account is locaked!'
			isLock = True
	if isLock ==True:
		break
	password = raw_input('password:').strip()

	if len(username) !=0 and len(password) !=0:
		f = file(account_file)
		loginSuccess = False
		for line in f.readlines(): 
			if username ==line.split()[0] and password == line.split()[1]:
				print 'welcome %s login my system!' % username
				loginSuccess = True
				break
		if loginSuccess is True:
			break
	else:
#		with open('lock_file','a') as f:
#			f.write('username\n')
		
		continue
	

