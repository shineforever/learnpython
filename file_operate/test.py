#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

with open("test.txt", "r") as f1:
	print(f1.read())
with open("test.txt", "r") as f2:
	# print(f.tell())
	# f.seek(27)
	# f.write("abc")
	f2.seek(5)
	print(f2.read())
	print(f2.tell())


