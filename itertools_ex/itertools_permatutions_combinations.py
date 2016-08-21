#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
itertools.permutations:排列
itertools.combinations:组合，需指定元素数
itertools.permutations_with_replacement:允许相同元素多次出现的组合
"""

from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement


l1 = [1, 2, 3, 4, 5]

# 打印所有可能的排列
for p in permutations(l1):
    print(p)

# 打印所有可能3位排列
for p in permutations(l1, 3):
    print(p)

# # 打印所有可能的组合,不考虑元素间的实际顺序，已选过的元素会被从候选元素中删除
# for i_c in combinations(l1, 5):
# 	print(i_c)
#
# # 打印所有可能的3位组合
# for i_c2 in combinations(l1, 3):
# 	print(i_c2)


# # 已选元素不会被从候选元素中删除
# for i_cr in combinations_with_replacement(l1, 5):
# 	print(i_cr)
#
# # 已选元素不会被从候选元素中删除
# for i_cr2 in combinations_with_replacement(l1, 3):
# 	print(i_cr2)


