#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
一些Pythonic的例子
"""

# 字典的默认值
# dict的get(key,default)方法用于获取字典中key的值，若不存在该key，则将key赋默认值default。
dic = {'name': 'Tim', 'age': 23}
dic['workage'] = dic.get('workage', 0) + 1
print(dic)

# 三元符的替代
a = 3
b = 2 if a > 2 else 1
print(b)

