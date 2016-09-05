#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
MyLogging Test
"""

import time
import logging
from log_demo import MyLogging  # 导入自定义的logging配置

logger = logging.getLogger(__file__)  # 生成logger实例


def demo():
    logger.debug("start range... time:{}".format(time.time()))
    for i in range(10):
        logger.debug("i:{}".format(i))
        time.sleep(2)
    else:
        logger.debug("over range... time:{}".format(time.time()))

if __name__ == "__main__":
    demo()
