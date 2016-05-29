#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com
"""
re 和 replace的区别
"""
import re
import string

# with open("english_demo.txt", "r", encoding="utf8") as f:
# 	for line in f:
# 		print("=" * 50)
# 		word = re.compile(r'[^a-zA-Z]')
# 		line = re.sub(word, line, " ")
# 		print(line)
# 		ignore_list = [",", ".", ";", "'", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# 		for i in ignore_list:
# 			line = line.replace(i, " ")
# 		print("^" * 50)
# 		print(line)

s = "I will do somebody a good turn and not get found out: If anybody knows of it, it will not count."

word = re.compile(r'[^a-zA-Z]')
s = re.sub(word, s, " ")
print(s)
print("*" * 50)
re.sub(word, s, " ")
print(s)
print(re.findall(r'[^a-zA-Z\s]', s))
s = re.sub(r'[^a-zA-Z\s]+', " ", s)
print(s)


# excule = set(string.punctuation)  # 获取所有的标点符号
# print(excule)
# word = re.compile("[{}]".format(string.punctuation))
#
# s = re.sub(word, " ", s)
# print(s)
