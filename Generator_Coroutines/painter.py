#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
假设有两个子程序 main 和 printer。
printer 是一个死循环，等待输入、加工并输出结果。
main 作为主程序，不时地向 printer 发送数据。
"""


def printer():
	counter = 0
	while True:
		string = (yield)
		print("[{0}] {1}".format(counter, string))
		counter += 1


if __name__ == "__main__":
	p = printer()
	next(p)
	p.send("Hi")
	p.send("My name is Q1mi.")
	p.send("Bye")

"""
这其实就是最简单的协程。程序由两个分支组成。
主程序通过 send 唤起子程序并传入数据，子程序处理完后，用 yield 将自己挂起，并返回主程序，如此交替进行。
"""
