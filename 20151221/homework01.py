#！/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "qimi"
'''
编写登录接口
-输入用户名密码
-认证成功后显示欢迎信息
-输错三次后锁定
'''

import sys
import getpass

account_file = "account.txt"
lock_file = "lock.txt"
lock_list = []
isLocked = False
loginSuccess = False

user_name = input("please input your user_name:").strip()	#去掉空格
with open(lock_file) as f1:
	for i in f1.readlines():
		i = i.strip()
		lock_list.append(i)
if user_name in lock_list:
	print("Sorry!%s were locked!"% user_name)
	isLocked = True
while not isLocked:
	with open(account_file) as f2:
		account_list = f2.readlines()
	for line in account_list:
		line = line.split()
		if user_name == line[0]:
			for i in range(3):
				pass_word = input("Password:")
				if pass_word == line[1]:
					print("Welcome to login!")
					loginSuccess = True
					isLocked = True
					break
			if loginSuccess is True:break
			else:
				with open(lock_file, 'at') as f:
					f.write('%s\n'% user_name)
				print("Too many tries!You will be locked!")
				isLocked=True
				break
		else:
			print("You haven't registered!\n")
			isLocked=True
			break
def function():
	pass