#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
Python Web编程实战（小绿书）里面学到的知识点
"""


# 1.使用next获取循环中符合条件的值
a1 = -1
for i in range(1, 10):
    if not i % 4:
        a1 = i
        break
print(a1)

a2 = next((i for i in range(1, 10) if not i % 4), -1)
print(a2)

# 2.执行调用直到某种情况结束
"""
blocks = []
while True:
    block = f.read(32)
    if block == "":
        break
    blocks.append(block)

"""


"""
from functools import partial
blocks = []
for block in iter(partial(f.read, 32), ""):
    blocks.append(block)
"""


