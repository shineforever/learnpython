#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

l1 = ["a", "b", "c"]
l2 = [1, 2, 3]
l3 = [4, 5, 6]

d1 = dict(list(zip(l2, l3)))
d = dict(list(zip(l1, d1.items())))
print(d1)
print(d)

