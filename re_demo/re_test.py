#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
正则的一些测试
计算器的作业中匹配数字的问题
"""

import re

r1 = re.compile(r'[+-]?\d*\.?\d+[*/][+-]?\d+\.?\d*')  # 这么写不能剔除.6 的情形


r2 = re.compile(r'[+-]?\d+(\.\d)?\d*[*/]-?\d+(\.\d)?\d*')  # 这么写就能剔除.6的情形


# \d+(\.\d)?\d*[*/]-?\d+(\.\d)?\d*

s1 = ".6*3"
s2 = "-987*654-(321/123+456*(-789*-98+76*(54/32)-101)*123)"

ret = r1.search(s1)
print(ret)
ret = r2.search(s1)
print(ret)
