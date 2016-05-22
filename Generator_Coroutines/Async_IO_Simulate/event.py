#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
异步IO模拟
"""
events_list = []


class Event(object):
	"""
	Event 是消息的基类，其在初始化时会将自己放入消息队列 events_list 中。
	Event 和 调度器 使用回调进行交互。
	"""
	def __init__(self, *args, **kwargs):
		self.callback = lambda: None
		events_list.append(self)

	def set_callback(self, callback):
		self.callback = callback

	def is_ready(self):
		result = self._is_ready()
		if result:
			self.callback()
		return result


