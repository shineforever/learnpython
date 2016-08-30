#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
some test
"""


class MyTest(object):
    def __init__(self, name):
        self.name = name

    def __unicode__(self):
        return "17"

    def __str__(self):
        return self.__unicode__()


a = MyTest(name="Alex")
print(a)
