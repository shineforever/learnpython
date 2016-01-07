#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]

n = list(zip(x, y, z))
print(n)

m = list(zip(*n))
print(m)

"""
在Python2.7里面实现跟上面同样的功能：
代码如下：
n = zip(x, y, z)
print(n)

m = zip(*n)
print(m)
"""
