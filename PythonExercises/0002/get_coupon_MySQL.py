#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）?
20160331：
	-将生成的激活码添加到MySQL数据库
		-初步表结构：
		│id│coupon│used│
		id:primary
		coupon:激活码
		used:是否已被使用的标志位
"""

import random
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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
# for t in range(200):
# 	a = get_coupon(16, 4)
# 	print(a)

engine = create_engine("mysql+pymysql://root:1234@localhost:3306/test03", echo=False)
Base = declarative_base()


# 存储激活码的表结构
class CouponTable(Base):
	__tablename__ = "coupon_table"
	id = Column(Integer, primary_key=True, autoincrement=True)
	coupon_info = Column(String(255), unique=True, nullable=False)
	used_state = Column(Boolean, nullable=False, default=False)

	def __repr__(self):
		return "<id={}, used_state={}>".format(self.id, self.used_state)


# 生成指定数量的激活码
def demo(amount):
	coupon_obj_list = []
	try:
		amount = int(amount)
		for c in range(amount):
			coupon_info = get_coupon(16, 4)
			coupon_obj = CouponTable(coupon_info=coupon_info)
			coupon_obj_list.append(coupon_obj)
	except TypeError as e:
		print("Error:", e)
	except Exception as e:
		print("Error:", e)
	finally:
		return coupon_obj_list


if __name__ == "__main__":
	Base.metadata.create_all(engine)  # 创建表结构
	Session = sessionmaker(bind=engine)
	session = Session()
	the_coupon_list = demo(200)
	session.add_all(the_coupon_list)  # 加入数据库
	session.commit()
