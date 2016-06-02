#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

from collections import Counter
import re
import atexit
import time
import math


def count_words(file, ignore_case=False):
	words_dic = {}
	with open(file, encoding="utf8") as f:
		words = re.compile(r'[^a-zA-Z\s]')
		for line in f:
			line = re.sub(words, " ", line)
			if ignore_case:
				line = line.lower()
			line_list = line.strip().split()
			line_dic = Counter(line_list)
			for word in line_dic:
				if word in words_dic:
					words_dic[word] += line_dic[word]
				else:
					words_dic[word] = line_dic[word]
	return words_dic


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


def main():
	a = count_words("english_Demo.txt", ignore_case=True)
	sorted_a = sorted(a.items(), key=lambda x: x[1], reverse=True)
	for i in sorted_a:
		print(i[0], i[1])
	print(type(sorted_a))


if __name__ == "__main__":
	main()
