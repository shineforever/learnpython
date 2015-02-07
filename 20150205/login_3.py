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
	username = raw_input('username:').strip()#remove the space
	lock_list = []
	f = file(lock_file)
	for i in f.readlines():
		h = i.strip('\n')#remove the line break
		lock_list.append(h)
	f.close()
#	print lock_list
	if username in lock_list:
		print 'Sorry!%s has been locked!' % username
		sys.exit()
	for line in account_list:
		line = line.split()#每一行以空格分开为line[0]和line[1]
		if username == line[0]:
			for i in range(3):
				password = raw_input('password:').strip()
				if password == line[1]:#password success
					print 'Welcome %s login my system!' % username
					loginSuccess = True
					break
			else:#三次输错，将用户名写入lock.txt
				f = file(lock_file,'a')
				f.write('%s\n' % username)
				f.close()
				print 'To many tries ,going to lock %s!'% username
				sys.exit()
  		if loginSuccess is True:break #jump out the 'for loop'
	if loginSuccess is True:break #jump out the 'while loop'
