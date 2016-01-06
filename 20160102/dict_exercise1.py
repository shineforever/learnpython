#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = zip(*([iter(a)] * 2))
for i in b:
	print(i)

# group_adjacent = lambda a, k: zip(*([iter(a)] * k))
# for i in group_adjacent(a, 3):
# 	print(i)

print("=" * 50)
m = iter(a)
for i in m:
	print(i)
print("-" * 50)

n = zip(*[iter(a)] * 4)
for i in n:
	print(i)

print("=" * 50)

print(a[::2])
print(a[1::2])
for i in zip(a[::2], a[1::2]):
	print(i)


def group_adjacent(x, y):
	return zip(*([iter(x)] * y))

for i in group_adjacent(a, 3):
	print(i)


print("*" * 50)
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
xyz = zip(x, y, z)
print(list(xyz))
u = zip(*xyz)
print("^" * 50)
print(list(u))

print("@" * 50)
t = zip((1, 4, 7), (2, 5, 8), (3, 6, 9))
print(list(t))
