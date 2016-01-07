#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
最近看到zip()的用法:

"""

a = [1, 2, 3, 4, 5, 6]

b = [iter(a)] * 2
print(b[0].__next__())
print(b[0].__next__())
print(b[1].__next__())
print(b[1].__next__())
print(len(b))

c = [iter(a)] * 5
print(c[0].__next__())
print(c[1].__next__())
print(c[2].__next__())
print(c[3].__next__())
print(c[4].__next__())
print(len(c))

