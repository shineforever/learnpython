#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

with open("test.txt", "r+") as f:
	# print(f.read(1))
	# print(f.tell())
	# f.seek(27)
	# f.write("abc")
	print(f.read())
	print(f.tell())


