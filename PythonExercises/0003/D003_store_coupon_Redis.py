#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
"""
import random
import redis


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


# 生成指定数量的激活码
def demo(amount):
	coupon_obj_list = []
	try:
		amount = int(amount)
		for c in range(amount):
			coupon_info = get_coupon(16, 4)
			coupon_obj_list.append(coupon_info)
	except TypeError as e:
		print("Error:", e)
	except Exception as e:
		print("Error:", e)
	finally:
		return coupon_obj_list

# 存储
r = redis.Redis(host="localhost", port=6379)
coupon_list = demo(200)
r.hmset("coupon", dict(zip(list(range(len(coupon_list))), coupon_list)))

# 查询
# for i in r.hgetall("coupon"):
# 	print(r.hget("coupon", i))
