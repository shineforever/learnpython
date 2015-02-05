#!/usr/bin/env python	
# -*- coding:utf8 -*-

import os
import sys

account_file = 'account.txt'
lock_file = 'lock.txt'

while True:
	f = file(account_file)
	account_list = f.readlines()
	f.close() 
	loginSuccess = False
	username = raw_input('username:').strip()
	lock_list = []
	f = file(lock_file)
	for i in f.readlines():
		h = i.strip('\n')
	lock_list.append(h)
	if username in lock_list:
		print 'Sorry!%s has been locked!' % username
		sys.exit()
	for line in account_list:
		line = line.split()
		if username == line[0]:
			for i in range(3):
				password = raw_input('password:').strip()
				if password == line[1]:
					print 'Welcome %s login my system!' % username
					loginSuccess = True
					break
			else:
				f = file(lock_file,'a')
				f.write('%s\n' % username)
				f.close()
				print 'To many tries ,going to lock %s!'% username
				sys.exit()
  		if loginSuccess is True:break #jump out the 'for loop'
	if loginSuccess is True:break #jump out the 'while loop'
