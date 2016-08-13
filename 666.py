#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
紫金葫芦 Pycharm使用指南

Date: 2016-08-02
Pycharm Version: 2016.2

"""


def test(num):
    """
    这是一个测试函数
    :param num: int类型参数
    :return: 打印一些偶数
    """
    for i in range(num):  # 代码后面的注释
        j = i + 1
        if j % 2 == 0:
            print(j)
    # 单独一行的注释
    else:
        print("The end.")

print("Hello World!")


def test2():
    pass


def test3():
    pass


class Test4(object):
    pass

if __name__ == "__main__":
    test(10)
