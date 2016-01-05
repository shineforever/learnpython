#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
题目：购物小程序
需求：程序启动后，要求用户输入购物预算，然后打印购物菜单，菜单格式如下：
Welcome to Alex's shopping mall,below are the things we are selling:
--------1. MacBook Air       7999
--------2. Starbucks Coffee  33
--------3. iphone 6 Plus     6188
--------4. ...
----用户可以不断的购买商品，程序要实时的把购买的商品添加到购物车，并且从预算金额中扣掉相应商品的价格，
----可购买的商品总值不能超过预算总值，用户选择退出后，打印他已购商品及所剩金额。
"""

from collections import OrderedDict
from collections import Counter

shop_dic = {"MacBook Air": 7999, "Starbucks Coffee": 33, "iphone 6 Plus": 6188, "Air Jordan S.F 4": 888, "Casio": 1799}

shopping_cart_list = []  # 定义购物车列表 用于记录所购物品。
while True:
	user_budget = input("请输入您的预算：").strip()
	if user_budget.isdigit():
		init_user_budget = user_budget = int(user_budget)
		break
	else:
		print("无效的输入请重新输入！")

# for i, key in enumerate(shop_dic, 1):
# 	print("%s. %-20s%10s" % (i, key, shop_dic[key]))    # 打印购物清单
# print("====================")

a = OrderedDict(sorted(shop_dic.items(), key=lambda t: t[1]))   # 价格从低到高排序成有序字典
print("Welcome to Q1mi's shopping mall,below are the things we are selling:")
for i, key in enumerate(a, 1):
	print("%s. %-20s%10s" % (i, key, a[key]))
	# 将脚标与价格对应起来

# 生成一个选项与物品名称及价格对应的字典
index_list = []
content_list = []
for i in range(1, len(a) + 1):
	index_list.append(i)
for j in a.items():
	content_list.append(j)
price_dict = dict(list(zip(index_list, content_list)))  # 字典格式：选项：(物品名称：价格)

while user_budget >= 0:    # 当用户的预算大于等于0时，就一直循环直到用户输入Q结算
	user_choose = input("请输入您的选择，Q结算退出：")
	if user_choose.isdigit():   # 判断输入是否为数字
		item_price = int(price_dict[int(user_choose)][1])
		if user_budget - item_price >= 0:   # 判断余额是否能购买所选的商品
			user_budget -= item_price    # 余额减去所选商品的价格

			# 判断购物车中是否有这个物品，如果有就在其数量上加1，如果没有就在购物车的字典里添加该物品，并把数量赋值为1
			# if price_dict[int(user_choose)[0] in shopping_cart:
			# 	shopping_cart.get(price_dict[int(user_choose)][1])
			# else:
			# 	shopping_cart[price_dict[int(user_choose)][0]] = 1

			object_name = price_dict[int(user_choose)][0]   # 定义物品名称
			shopping_cart_list.append(object_name)  # 将用户选择的物品名称加入购物车列表
			print("%s已加入购物车，Q结算退出：" % price_dict[int(user_choose)][0])
			print("您当前余额：%s" % user_budget)
		else:
			print("余额不足！")
			print("您当前余额：%s" % user_budget)
	elif user_choose.upper() == 'Q':
		print("正在结算，请稍后...")
		print("=" * 75)
		print("您的预算总额是：%60s" % init_user_budget)
		shopping_cart_count = Counter(shopping_cart_list)   # Counter统计序列中元素出现的次数
		for key, val in shopping_cart_count.items():
			print("商品名称：%-20s 数量：%-10s 单价：%-10s 总价：%-10s" % (
				key, shopping_cart_count[key], a[key], a[key] * shopping_cart_count[key]))
		print("=" * 75)
		print("打印出购物车中的物品名称及数量")
		break
	else:
		print("无效的输入，请重新输入！")
