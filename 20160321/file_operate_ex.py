#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
问：
1、文件不能第二次写入
2、count只有第一次会得到正确结果，之后就一直为0了
答：
第一次循环完之后，指针就指到最后了，下一次循环开始前需要把指针移到文件开头位置。

再问：
现在 文件f是10G
我怎么在最快的速度内匹配到我所需要的内容
并按照匹配的顺序.写入 f2

多线程并发去取、去匹配
"""

with open("keepalived.log", "r") as f:
	times = 0
	while True:
		count = 0
		search = input("please enter the one you want:")

		print("\033[42;1mTimes:<{}>   Wanted:<{}>.\033[0m".format(times, search))

		for i in f.readlines():
			if search in i:
				# print("Find it!")
				count += 1
				with open("record.txt", "a") as f2:
					for row in i:
						f2.write(row)
			# else:
		        # print("Can't find.")
		else:
			times += 1
			# 文件循环完了，把指针移回到开始处，以便下次循环
			f.seek(0)
		with open("record.txt", "r") as f2:
			for t in f2.readlines():
				print(t)

		print(count)
		print("=" * 60)
