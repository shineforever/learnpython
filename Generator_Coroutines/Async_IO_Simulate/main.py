#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
主代码
"""

from sleep import sleep
import runner


def task(name):
	print(name, 1)
	yield sleep(1)
	print(name, 2)
	yield sleep(2)
	print(name, 3)
	yield sleep(3)


if __name__ == "__main__":
	runner.run((task("Q1mi"), task("Jack")))
