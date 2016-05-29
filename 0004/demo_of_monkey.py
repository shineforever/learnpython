#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

# 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
import operator


def get_count_table(filename, lower=True):
	ignore = [',', '.', ':', '!', '?', '”', '“', ";", '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	with open(filename, "r", encoding="utf8") as f:
		for line in f:
			for i in ignore:
				line = line.replace(i, ' ')
			if lower:
				line = line.lower()
			words = line.strip().split(' ')
			dic = {}
			for word in words:
				if word is '':
					continue
				if word in dic:
					dic[word] += 1
				else:
					dic[word] = 1
			return dic


a = get_count_table('english_demo.txt')
result = sorted(a.items(), key=operator.itemgetter(1), reverse=True)
# result = sorted(a.items(), key=lambda x: x[1], reverse=True)
for item in result:
	print(item[0], item[1])
