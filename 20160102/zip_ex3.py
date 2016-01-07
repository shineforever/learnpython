#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

a = [1, 2, 3, 4, 5, 6]
b = list(zip(*[iter(a)] * 2))
print(b)

x = [1, 3, 5]
y = [2, 4, 6]
t = list(zip(*[x, y]))
print(t)

print([x, y] == list([iter(a)] * 2))
print([x, y] == [iter(a)] * 2)
