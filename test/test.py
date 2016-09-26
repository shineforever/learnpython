#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

import string
import random
import os
import re
import json

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
# p1 = re.compile(r'\^ab')
# print(p1.findall('^abAB  ^abc ccc ABc'))

# 按行打印
# with open("test", "r+") as f:
#     for line in f:
#         print(f.tell())
#         print(line.strip())

# 写入测试
# l = ["A", "B", "C"]
# l2 = ["张", "三", "李", "四"]
# with open("test.json", "") as f:
#     acc = json.load(f)
#     ind = acc["user"].index("zhangsan")
#     acc["locked_flag"][ind] = 1
#     json.dump(acc, f, ensure_ascii=False)

import menu_demo




