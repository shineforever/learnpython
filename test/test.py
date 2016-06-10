#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

import string
import random
import os
import re

# print(string.ascii_letters)
# print(string.printable)

# list1 = [1, 2, 1, 2, 3, 5, 9]
# list1.sort(reverse=True)
# print(list1)


# 随机取10个100-200之间的数
# print(random.sample(range(100, 200), 10))
# print(random.randrange(range(100, 200), 10))

# 打印当前目录
# print(os.getcwd())

# 忽略大小写，取短
# p = re.compile(r'ab*', re.I)
# print(p.findall('abAB'))

# 匹配字符串^ab
p1 = re.compile(r'\^ab')
print(p1.findall('^abAB  ^abc ccc ABc'))
