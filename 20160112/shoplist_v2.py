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

	* version2.0 优化程序布局
	* 2016.01.12
"""

from collections import OrderedDict
from collections import Counter


def get_budget():
	while True:
		user_budget = input("请输入您的预算：").strip()    # 获取用户输入的预算
		if user_budget.isdigit():
			user_budget = int(user_budget)
			return user_budget
		else:
			print("无效的输入请重新输入！")


# 初始化商品目录
def init_shop_dic():
	shop_dic = {"MacBook Air": 7999, "Starbucks Coffee": 33, "iphone 6 Plus": 6188, "Air Jordan S.F 4": 888, "Casio": 1799}
	return OrderedDict(sorted(shop_dic.items(), key=lambda t: t[1]))   # 价格从低到高排序成有序字典
	print("Welcome to Q1mi's shopping mall,below are the things we are selling:")


# 打印商品列表
def print_shop_dic():
	global ORDERED_SHOP_DIC
	for i, key in enumerate(ORDERED_SHOP_DIC, 1):
		print("%s. %-20s%10s" % (i, key, ORDERED_SHOP_DIC[key]))   # 打印出序号与物品名称及价格


# 生成一个选项与物品名称及价格对应的字典
def get_price_dict():
	global ORDERED_SHOP_DIC
	index_list = []
	content_list = []
	for i in range(1, len(ORDERED_SHOP_DIC) + 1):
		index_list.append(i)
	for j in ORDERED_SHOP_DIC.items():
		content_list.append(j)
	return dict(list(zip(index_list, content_list)))  # 字典格式：选项：(物品名称：价格)


# 结算
def check_out():
	global INIT_USER_BUDGET
	print("正在结算，请稍后...")
	print("=" * 75)
	print("您的预算总额是：%60s" % INIT_USER_BUDGET)    # 打印用户最开始输入的预算
	print("-" * 75)
	print("您的购物清单如下：")
	print("-" * 75)
	shopping_cart_count = Counter(shopping_cart_list)   # Counter统计序列中元素出现的次数
	for key, val in shopping_cart_count.items():    # 打印出用户的购物清单
		print("商品名称：%-20s 数量：%-10s 单价：%8s 总价：%8s" % (
			key, shopping_cart_count[key], ordered_shop_dic[key], ordered_shop_dic[key] * shopping_cart_count[key]))
	print("-" * 75)
	print("您的余额：%66s" % user_budget)
	print("=" * 75)
	print("谢谢惠顾！")


# 判断选择
def get_choose():
	if user_choose.isdigit():   # 判断输入是否为数字
		user_choose = int(user_choose)  # 将用户输入转为int类型
		if 0 < user_choose <= len(ordered_shop_dic):   # 判断输入是否为有效数字
			item_price = int(price_dict[user_choose][1])   # 找到用户选择物品的价格
			if user_budget - item_price >= 0:   # 判断余额是否能购买所选的商品
				user_budget -= item_price    # 获取余额
				object_name = price_dict[user_choose][0]   # 定义物品名称
				shopping_cart_list.append(object_name)  # 将用户选择的物品名称加入购物车列表
				print("%s已加入购物车，Q结算退出：" % price_dict[user_choose][0])
				print("您当前余额：%s" % user_budget)
			else:
				print("余额不足！")
				print("您当前余额：%s" % user_budget)
		else:   # 输入无效的数字打印提示
			print("无效的输入，请重新输入！")
	elif user_choose.upper() == 'Q':
		check_out()
	else:
		print("无效的输入，请重新输入！")


def main():
	INIT_USER_BUDGET = USER_BUDGET = get_budget()
	ORDERED_SHOP_DIC = init_shop_dic()
	print_shop_dic()
	PRICE_DICT = get_price_dict()
	while USER_BUDGET >= 0:    # 当用户的预算大于等于0时，就一直循环直到用户输入Q结算
		USER_CHOOSE = input("请输入您的选择，Q结算退出：")
		get_choose()


if __name__ == '__main__':
	main()
