#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
通过自定义 sleep 我们可以模拟异步延时操作
"""
from event import Event
from time import time


class SleepEvent(Event):

	def __init__(self, timeout):
		super(SleepEvent, self).__init__(timeout)
		self.timeout = timeout
		self.start_time = time()

	def _is_ready(self):
		return time() - self.start_time >= self.timeout


def sleep(timeout):
	"""
	sleep 在调用后就会立即返回，同时一个 SleepEvent 对象会被放入消息队列，经过timeout 秒后执行回调。
	:param timeout:
	:return:
	"""
	return SleepEvent(timeout)
