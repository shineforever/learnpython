#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
处理log
"""

import time
from log_demo import timethis


def log_handler(filename):
    """
    遍历日志的每一行，取出记数
    :param filename:
    :return:
    """
    with open(filename, "r") as f:
        for line in f:
            time_num = line.split()[3]
            time_str = time_num.split(":")[-1]
            yield int(time_str)


if __name__ == "__main__":
    start = time.time()
    log_ = log_handler("test.log")
    log_list = list(log_)
    print(sum(log_list))
    end = time.time()
    print("total time:", end-start)
