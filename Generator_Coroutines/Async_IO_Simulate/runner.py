#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
协程调度
run 启动了所有的子程序，并开始消息循环。
每遇到一处挂起，调度器自动设置回调，并在回调中重新恢复代码流。
"""

from event import events_list


def run(tasks):
	for task in tasks:
		_next(task)

	while len(events_list):
		for event in events_list:
			if event.is_ready():
				events_list.remove(event)
				break


def _next(task):

	try:
		event = next(task)
		event.set_callback(lambda: _next(task))  # 利用闭包保存状态
	except StopIteration:
		pass
