#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
多线程测试
"""

import threading
import requests

url_list = [
    "http://www.baidu.com",
    "http://www.liwenzhou.com",
    "https://www.baidu.com",
    "https://www.baiduxxxxx.com",
    "http://www.jd.com",
    "http://jr.jd.com",
    "http://vip.jd.com",
]


def http_check(url):
    try:
        res = requests.get(url=url, timeout=1)
        if res.status_code == 200:
            print("\033[32;42m{}\033[0m:OK!".format(url))
        else:
            print("{}:ERROR!".format(url))
    except Exception as e:
        print("\033[31;41m{}\033[0m".format(url))
        print(str(e))


if __name__ == "__main__":
    # for url in url_list:
<<<<<<< HEAD
    #     t = threading.Thread(target=http_check, args=(url,))
    #     t.start()
=======
    # 	t = threading.Thread(target=http_check, args=(url,))
    # 	t.start()
>>>>>>> b0142050f9b38e12d9a12938e3e8f509fadc10c3
    r = map(http_check, url_list)

