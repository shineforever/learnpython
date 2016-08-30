#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/8/17

"""
生成器的使用场景
"""

list_demo = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_even(the_list):
    """
    一个只为产生list然后返回的函数
    :param the_list:
    :return:
    """
    even_list = []
    for i in the_list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


def get_even2(the_list):
    """
    使用yield动态返回值
    :param the_list:
    :return:
    """
    for i in the_list:
        if i % 2 == 0:
            yield i


def get_square(the_list):
    """
    接收一个列表作为参数，进行一系列操作的函数
    :param the_list:
    :return:
    """
    for i in the_list:
        print(i*i)


if __name__ == "__main__":
    a = get_even2(list_demo)
    get_square(a)

