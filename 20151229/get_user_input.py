#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"


def get_user_input(level_num, level_list):
	while True:
		if level_num == 1:
			user_input = input("请输入相应数字，'Q'退出本系统：").strip()
			if user_input.isdigit():
				user_input = int(user_input)
				if user_input <= len(level_list):
					return level_list[user_input - 1]
				else:
					print("无效的输入，请重新输入！")
			elif user_input.upper() == 'Q':
				return 'Q'
			else:
				print("无效的输入，请重新输入！")
		elif level_num == 2 or level_num == 3:
			user_input = input("请输入相应数字，'B'回到上一级菜单，'Q'退出本系统：").strip()
			if user_input.isdigit():
				user_input = int(user_input)
				if user_input <= len(level_list):
					return user_input
				else:
					print("无效的输入，请重新输入！")
			elif user_input.upper() == 'B':
				return 'B'
			elif user_input.upper() == 'Q':
				return 'Q'
			else:
				print("无效的输入，请重新输入！")
		else:
			print("参数错误！")
