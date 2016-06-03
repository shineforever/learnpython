#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
从一个列表中找出三个元素的和最接近与给定的值
"""

import random

l1 = [random.randrange(100) for i in range(100)]

print(l1)


def shift_down(lst, start, end):
	root = start
	while True:
		child = 2 * root + 1  # 左孩子
		if child > end:
			break
		if child+1 <= end and lst[child+1] > lst[child]:
			child += 1
		if lst[child] > lst[root]:
			lst[child], lst[root] = lst[root], lst[child]
			root = child
		else:
			break


def heap_sort(lst):
	for i in range(len(lst)//2, -1, -1):  # 从最后一个有child的节点开始往前循环直到0
		shift_down(lst, i, len(lst)-1)

	for j in range(len(lst)-1, 0, -1):  # 相当于循环len(lst)次
		lst[0], lst[j] = lst[j], lst[0]  # 把最大的放到堆最后，然后继续排序剩下的list
		shift_down(lst, 0, j-1)  # 不断的减小要排序的堆
	return lst

heap_sort(l1)
print(l1)

s = 123

# l1中找出三个数，使其和最接近s


def find_three(lst, goal):
	closed = (float("inf"), )
	closed_value = float("inf")
	for i in range(len(lst)-2):
		j = i+1
		k = len(lst)-1
		while j < k:
			tmp = tuple(lst[x] for x in (i, j, k))
			value_tmp = abs(sum(tmp) - goal)
			if value_tmp == 0:
				return tmp
			else:
				if value_tmp < closed_value:
					closed_value = value_tmp
					closed = tmp
					if sum(tmp) - goal > 0:
						k -= 1
					else:
						j += 1
				else:
					break

		return closed


def main():
	ll = [1, 3, 5, 7, 9]
	ss = 17
	ret = find_three(ll, ss)
	print(ret)

if __name__ == "__main__":
	main()
