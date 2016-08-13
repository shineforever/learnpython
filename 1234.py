#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
1、2、3、4能构成多少个互不相同且无重复的三位数，都是多少？
"""
l1 = []
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j != k and i != k:
                l1.append("{}{}{}".format(i, j, k))
                # print("{}{}{}".format(i, j, k))
print(len(l1))
for i in l1:
    print(i)


