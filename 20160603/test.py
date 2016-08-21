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

s = 223

# l1中找出三个数，使其和最接近s


def find_three(lst, goal):
    closed = (float("inf"), )  # 定义一个无穷大的元祖，存放要得到的三个数
    closed_value = float("inf")  # 定义一个用于存储任意三个数的和与目标数的差值（绝对值）
    for i in range(len(lst)-2):
        j = i+1
        k = len(lst)-1
        while j < k:
            tmp = tuple(lst[x] for x in (i, j, k))  # 得到三个元素组成的元祖
            value_tmp = abs(sum(tmp) - goal)  # 得到三元素的和与目标数的差值的绝对值
            if value_tmp == 0:  # 如果三个元素的和等于目标数，返回该三个元素
                return tmp
            else:
                if value_tmp < closed_value:  # 如果差值小于上一个差值
                    closed_value = value_tmp  # 保存这一次的差值
                    closed = tmp  # 保存当前的三个元素
                if sum(tmp) - goal > 0:  # 如果三元素的和比目标数大，
                    k -= 1  # K往前取值（即要往小的找）
                else:
                    j += 1  # 如果三元素的和比目标数小，j往后取（即要找个大的值）

        return closed


def main():
    # ll = [1, 3, 5, 7, 9, 13, 19, 22, 34, 35]
    # ss = 23
    ret = find_three(l1, s)
    print(ret)

if __name__ == "__main__":
    main()
