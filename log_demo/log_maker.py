#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
生成log数据
"""

import time


LOG_FORMAT = '80.154.42.54 - - [23/Aug/2010:{time} +0000] "GET /phpmy-admin/scripts/setup.php HTTP/1.1" " 404 347 "-" "ZmEu"'


def write_log(filename, nums):
    count = 0
    with open(filename, "w") as log_f:
        while count < nums:
            time_stamp = "{}:{}".format(time.ctime().split()[3], count)
            log_f.write(LOG_FORMAT.format(time=time_stamp) + "\n")
            count += 1


if __name__ == "__main__":
    write_log("test1.log", 10)
