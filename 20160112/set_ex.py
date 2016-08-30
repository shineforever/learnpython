#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
集合（set）的内建功能练习
集合（set）是一个无序且不重复的元素的集合。
"""

s1 = {1, 2, 3, 3}
print(s1)

# add(self, *args, **kwargs) 给集合添加一个新的元素
s1.add(4)
s1.add((4, 5))
print(s1)

# clear(self, *args, **kwargs) 移除集合内的所有元素
s1.clear()
print(s1)

# copy 返回一个集合的浅拷贝
s1 = {1, 2, 3}
s2 = s1.copy()
print(s2)

# difference() 返回两个或多个集合之间不同的元素的集合
s1 = {1, 2, 3}
s2 = {1, 3, 5}
s4 = {2, 4, 6, 8}
s3 = s1.difference(s2)  # 把s1里有的，s2里没有的返回给s3
s5 = s4.difference(s1)  # 把s4里有的，s1里没有的返回给s5
s = "s1:{0}\ns2:{1}\ns3:{2}\ns4:{3}"
print(s.format(s1, s2, s3, s5))

# difference_update()   # 从集合里移除另一个集合里的所有元素
s4.difference_update(s1)    # 从s4里面移除s1里也有的所有元素
print(s4)

# discard() 移除集合里的一个元素，如果给的参数不是集合里的元素，则什么都不做
s4.discard(2)
print(s4)
s4.discard(4)
print(s4)

# intersection() 返回两个集合的交集的集合
s1 = {1, 2, 3}
s2 = {1, 3, 5}
s3 = s1.intersection(s2)
print(s3)

print('line:52'.center(20, '*'))
# intersection_update() sa.intersection_update(sb):用sa和sb的交集返回给sa
s1 = {1, 2, 3}
s2 = {1, 3, 5}
s1.intersection_update(s2)
print(s1)

# isdisjoint() # 判断两个集合有无交集，无交集返回True
s1 = {1, 2, 3}
s2 = {1, 3, 5}
s3 = {2, 4, 6}
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s3))

# issubset() sa.issubset(sb):判断sa是否为sb的子集
s1 = {1, 3, 5}
s2 = {1, 3}
print(s2.issubset(s1))

# issuperset sa.issuperset(sb):判断sa是否包含sb
print(s1.issuperset(s2))

# pop() 移除并返回一个任意元素，集合为空时会raise KeyError
s1 = {1, 3, 5}
print(s1.pop())
print(s1)

# remove() 从集合中移除一个元素，没有此元素时,raise KeyError
s1 = {1, 3, 5}
s1.remove(3)
print(s1)

print('line:84'.center(30, '*'))

# symmetric_difference()    返回两个集合的非交集元素到一个新集合
s1 = {1, 2, 5}
s2 = {1, 3, 5, 7}
s3 = s1.symmetric_difference(s2)
print(s3)

# symmetric_difference_update()     sa.symmetric_difference_update(sb):将sa、sb的非交集元素返回给sa
s1 = {1, 2, 5}
s2 = {1, 3, 5, 7}
s1.symmetric_difference_update(s2)
print(s1)

# union() sa.union(sb):返回sa、sb的合集
s1 = {1, 2, 3}
s2 = {1, 3, 5}
s3 = s1.union(s2)
print(s3)

# update() sa.update(sb):将sa、sb的合集返回给sa
s1 = {1, 3, 5}
s2 = {2, 4, 6}
s1.update(s2)
print(s1)


