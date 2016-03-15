#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
a bottle demo
"""

from bottle import route, run, template


# route是一个将代码绑定到地址的装饰器，从而把‘/hello’连接到hello()方法。，
@route('/hello/<name>')
def index(name):
	return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)

