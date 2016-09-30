#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9999)
