#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
本周一的时间
"""

import time
import datetime

now = time.time()
print(now)
print(type(now))

now1 = datetime.date.today()
w = now1.weekday()
print(w)
date_delta = datetime.timedelta(days=w)
print(now1)
this_monday = now1 - date_delta
print(this_monday)
this_monday_stamp = time.mktime(this_monday.timetuple())
print(type(this_monday_stamp))

print(now > this_monday_stamp)