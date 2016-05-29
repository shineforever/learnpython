#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）?
"""

import random

# coupon = ""
# 生成16位的优惠券
# for i in range(16):
# 	current = random.randrange(0, 16)
# 	if current != i:
# 		temp = chr(random.randint(65, 90))
# 	else:
# 		temp = random.randint(1, 9)
# 	coupon = "{}{}".format(coupon, temp)
#
# print(coupon)


def get_coupon(total_count, num_count):
	"""
	获得总长为total_count,包含num_count位数字的随机码
	:param total_count:总长度
	:param num_count: 数字的个数
	:return:
	"""
	coupon = ""
	# 先生成一个指定位数的随机字母序列
	for i in range(total_count):
		temp1 = chr(random.randint(65, 90))
		coupon = "{}{}".format(coupon, temp1)

	coupon_list = list(iter(coupon))
	# 再随机生成指定位数的数字去随机替换上面序列中的字母
	for j in range(num_count):
		temp2 = random.randint(0, 9)    # 随机出一个数字
		temp3 = random.randint(0, total_count - 1)      # 随机一个索引
		coupon_list[temp3] = str(temp2)     # 用数字去替换索引位的值
	# 返回最终生成的随机码
	return "".join(coupon_list)

# 生成两百个随机码
for t in range(200):
	a = get_coupon(16, 4)
	print(a)



