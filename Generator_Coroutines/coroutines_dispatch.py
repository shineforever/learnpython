#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
协程调度
"""
from collections import deque


def task(name, times):
	for i in range(times):
		yield
		print(name, i)

"""
这里的 yield 没有逻辑意义，仅是作为暂停的标志点。
程序流可以在此暂停，也可以在此恢复。
而通过实现一个调度器，我们可以完成多个任务的并行处理：
"""


class Runner(object):
	def __init__(self, tasks):
		self.tasks = deque(tasks)

	def next(self):
		return self.tasks.pop()

	def run(self):
		"""
		通过轮转队列依次唤起任务，并将已经完成的任务清出队列，简洁地模拟了任务调度的过程。
		:return:
		"""
		while len(self.tasks):
			task = self.next()
			try:
				next(task)
			except StopIteration:
				pass
			else:
				self.tasks.appendleft(task)

tasks_list = [task("Q1mi", 6), task("Jack", 5), task("Bob", 4)]
Runner(tasks_list).run()

