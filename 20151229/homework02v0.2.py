#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

'''
多级菜单
-三级菜单
-可依次选择进入各子菜单
-所需新知识点：列表、字典
'''

import sys
import get_user_input


city_dict = {
	"北京": {
		"朝阳区": ["国贸", "望京", "三里屯"],
		"海淀区": ["五道口", "中关村", "学院路"],
		"昌平区": ["沙河", "天通苑", "回龙观"]
	},
	"上海": {
		"静安区": ["静安寺", "梅恒泰", "大中里太古城"],
		"黄浦区": ["人民广场", "外滩", "豫园"],
		"徐汇区": ["中山公园", "天山路商圈", "古北路商圈"]
	},
	"香港": {
		"旺仔": ["铜锣湾", "跑马地", "大坑"],
		"油尖旺": ["尖沙咀", "旺角", "佐敦"],
		"西贡": ["清水湾", "将军澳", "北潭涌"]
	}
}

level1_list = []
level2_list = []


print("第一级目录：")
for i in iter(city_dict):
	level1_list.append(i)   # 生成第一级菜单的列表
for i in level1_list:
	print("%s.%s" % (level1_list.index(i)+1, i))  # 打印出一级菜单

a = get_user_input.get_user_input(1, level1_list)
print(type(a))
if a == 'Q':
	print("您的选择是退出本系统！")
	sys.exit()
else:
	print("您的选择是%s" % a)
	print("%s的子目录是：" % a)
	for i in iter(city_dict[a]):
		level2_list.append(i)
	for i in level2_list:
		print("%s.%s" % (level2_list.index(i) + 1, i))  # 打印对应的二级目录
	b = get_user_input.get_user_input(2, level2_list)
	if b == 'Q':
		print("您的选择是退出本系统！")
		sys.exit()
	elif b == 'B':
		print("您的选择是回到上一级菜单！")

#
# 	user_input2 = input("请输入您的选择，按B退回上级，按Q退出：").strip()
# 	if user_input2.isdigit():
# 		user_input2 = int(user_input2)    # 如果用户输入的是数字就把输入变成'int'类型
# 		if user_input2 <= len(level2_list):  # 判断输入是否为有效数字
# 			m1 = level2_list[user_input2 - 1]
# 			print("您的选择是：%s" % m1)
# 			print("%s的下一级菜单：" % m1)
# 			for i in city_dict[m][m1]:
# 				print("%s.%s" % (city_dict[m][m1].index(i)+1, i))  # 打印出对应的三级菜单
# 		else:
# 			print("错误的输入！")
# 	elif user_input.upper() == 'B':
# 		print("退出本级菜单...")
# 	elif user_input.upper() == 'Q':
# 		print("退出程序...")
# 	else:
# 		print("Bad input!!!")
#
# else:
# 	sys.exit()