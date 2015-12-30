#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Q1mi"

i_count = 0
while i_count < 3:
	username = input("账号：")
	userpasswd = input("密码：")
	name = open("namepwd.txt", "r")

	for i in name.readlines():
		if username == i.split()[0] and userpasswd == i.split()[1]:
			print("OK")
			i_count = 3
			break   # 跳出for循环
	else:
		print("No")
	i_count += 1
