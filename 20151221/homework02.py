#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Q1mi"

'''
多级菜单
-三级菜单
-可依次选择进入各子菜单
-所需新知识点：列表、字典
'''

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
level1_list = city_dict.keys()
print(type(level1_list))
level2_list = city_dict["北京"].keys()
print(type(level2_list))
level3_list = city_dict["北京"]["朝阳区"]
print(type(level3_list))
print("第一级目录：")
n = 1
for item in city_dict:
	print("%s.%s" % (n, item))
	n += 1
user_choice = input("请输入您的选择，按Q退出：").strip()
if user_choice == "Q":
	pass
elif user_choice == "":
	pass
else:
	print("Sorry!Bad input!")
print("第二级目录：")
n = 1
for item in city_dict["北京"]:
	print("%s.%s" % (n, item))
	n += 1
print("第三级目录：")
n = 1
for i in level3_list:
	print("%s.%s" % (n, i))
	n += 1
