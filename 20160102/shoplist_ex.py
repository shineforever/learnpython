#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
	题目：购物小程序
	需求：程序启动后，要求用户输入购物预算，然后打印购物菜单，菜单格式如下：
	Welcome to Alex's shopping mall,below are the things we are selling:
		1. MacBook Air       7999
		2. Starbucks Coffee  33
		3. iphone 6 Plus     6188
		4. ...
	用户可以不断的购买商品，程序要实时的把购买的商品添加到购物车，并且从预算金额中扣掉相应商品的价格，
	可购买的商品总值不能超过预算总值，用户选择退出后，打印他已购商品及所剩金额。
"""

shop_dic = {
	"MacBook Air": 7999, "Starbucks Coffee": 33, "iphone 6 Plus": 6188, "Air Jordan S.F 4": 888, "Casio": 1799
}

while True:
	user_budget = input("请输入您的预算：").strip()
	if user_budget.isdigit():
		user_budget = int(user_budget)
		break
	else:
		print("无效的输入请重新输入！")

for i, key in enumerate(shop_dic, 1):
	print("%s. %-20s%10s" % (i, key, shop_dic[key]))    # 打印购物清单

