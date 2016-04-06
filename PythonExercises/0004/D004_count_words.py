#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
任一个英文的纯文本文件，统计其中的单词出现的个数
"""

from collections import Counter
import time
import math
import atexit
import re
import operator


def count_words(arg):
	with open(arg, "rt", encoding="utf8") as f:
		words = re.compile(r'[^a-zA-Z\s]')
		count_dic = {}
		for line in f:
			line = re.sub(words, " ", line)
			line_list = line.strip().split()
			line_dic = Counter(line_list)
			for key in line_dic:
				if key in count_dic:
					count_dic[key] += line_dic[key]
				else:
					count_dic[key] = line_dic[key]
	return count_dic


# atexit模块可以让你在脚本运行完后立马执行一些代码
# 此处用于测量脚本的运行时间。
def microtime(get_as_float=False):
	if get_as_float:
		return time.time()
	else:
		return "{} {}".format(*math.modf(time.time()))
start_time = microtime(False)
atexit.register(microtime)


def shutdown():
	global start_time
	print("Execution took: {0} seconds".format(start_time))

atexit.register(shutdown)


if __name__ == "__main__":
	a = count_words("english_demo.txt")
	sort_a = sorted(a.items(), key=lambda x: x[1], reverse=True)
	for item in sort_a:
		print(item[0], item[1])
	print(type(sort_a))
