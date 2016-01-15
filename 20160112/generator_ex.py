#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
生成器(generator)的练习
generator 基于yield建立，即生成器在使用时才创建，避免内存浪费。
"""

"""练习：
<br>有如下列表：[13, 22, 6, 99, 11]
请按照一下规则计算：
13 和 22 比较，将大的值放在右侧，即：[13, 22, 6, 99, 11]
22 和 6 比较，将大的值放在右侧，即：[13, 6, 22, 99, 11]
22 和 99 比较，将大的值放在右侧，即：[13, 6, 22, 99, 11]
99 和 42 比较，将大的值放在右侧，即：[13, 6, 22, 11, 99,]
...
13 和 6 比较，将大的值放在右侧，即：[6, 13, 22, 11, 99,]
"""


l1 = [13, 22, 6, 99, 11]
for i in range(len(l1) - 1):    # 取左边的数
	for j in range(i+1, len(l1)):   # 取右边的数
		if l1[i] > l1[j]:   # 左右比较
			l1[i], l1[j] = l1[j], l1[i]    # 左右交换位置
print(l1)
