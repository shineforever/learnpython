#！/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "qimi"
'''
编写登录接口
-输入用户名密码
-认证成功后显示欢迎信息
-输错三次后锁定
'''
import os
import sys

account_file = "account.txt"
lock_file = "lock.txt"
isLocked = False

user_name = input("please input your user_name:").strip()	#去掉空格
with open(account_file) as f1:
	account_list = f1.readlines()
	for i in ff.readlines():
		i = i.strip()
		account_list.append(i)
if user_name in lock_list:
	print("Sorry!%s were locked!"% user_name)
	isLocked = True
	sys.exit(0)
while not isLocked:
	with open(account_file) as f:
		account_list = f.readlines()
	for line in account_list:
		line = line.split()
		if user_name == line[0]:
			for i in range(3):
				pass_word = input("Passwd:")
				if pass_word == line[1]:
					print("Welcome to login!")
					break
			else:
				with open(lock_file, 'a') as f:
					f.write('%s\n'% user_name)
					print("Too many tries!You will be locked!")
				sys.exit(0)
		else:
			print("You haven't registered!")
			break
