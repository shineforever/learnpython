#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
map()、filter()和reduce()
"""
from functools import reduce

# map()函数接收两个参数，一个是函数，一个是Iterable。
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

"""
小练习
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
"""


def normaliza(name):
    name = name.title()
    return name

l1 = ['adam', 'LISA', 'barT']
l2 = list(map(normaliza, l1))
print(l2)

# 更Pythonic的方法
l3 = list(map(str.title, l1))
print(l3)


# filter的练习,找出列表中大于50的元素
l1 = [12, 33, 54, 6, 48, 98]
l2 = list(filter(lambda t: t > 50, l1))
print(l2)




"""
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
"""


def prod(l):
    return reduce(lambda x, y: x * y, l)

print('3*5*7*9=', prod([3, 5, 7, 9]))

"""
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
"""


def str2float(s):
    m = s.split('.')
    i1 = list(map(int, m[0]))
    i2 = list(map(int, m[1]))
    i2.reverse()
    f1 = reduce(lambda x, y: x*10+y, i1)
    f2 = reduce(lambda x, y: x*0.1+y, i2)
    return f1+f2/10

print('字符串转换成浮点数=>', str2float('123.456'))
print('字符串转换成浮点数=>', str2float('654.321'))
