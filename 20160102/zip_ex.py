#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]

xyz = zip(x, y, z)
print(list(xyz))
# zip(*xyz) 等价于 zip((1, 4, 7), (2, 5, 8), (3, 6, 9)) ???

u = zip(*xyz)
print(u)

t = zip((1, 4, 7), (2, 5, 8), (3, 6, 9))
print(list(t))
