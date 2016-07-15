#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
面向对象一些测试
类属性
"""


class A(object):
	str1 = "aaa"

	def __init__(self):
		A.str1 = "bbb"
		print(A.str1)
	print(u"我在构造方法外！")


a = A()
print(A.str1)
