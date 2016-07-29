#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com


import urllib.request
from bs4 import BeautifulSoup


root_url = "http://www.njgs.gov.cn/zxfw/kscx/szqycx"
url_2 = "http://www.njgs.gov.cn/zxfw/kscx/szqycx/index_1.html"
# 第一页是http://www.njgs.gov.cn/zxfw/kscx/szqycx
# 第二页是http://www.njgs.gov.cn/zxfw/kscx/szqycx/index_1.html


def get_url(page_num):
	"""
	我写了个方法，来组合url
	:param page_num:
	:return:
	"""
	return "{}/index_{}.html".format(root_url, page_num)


def get_data(url):
	"""
	爬取数据
	:param url:
	:return:
	"""
	req = urllib.request.Request(url)
	try:
		response = urllib.request.urlopen(req)
		soup = BeautifulSoup(response, "html.parser")
		list1 = soup.find_all("tr", class_="qycx2")
		# print(soup.find(id="conList"))
		return list1
	except Exception as e:
		print(e)


def get_info_list(str_list):
	ret_list = []
	for i in str_list:
		info_str = i.get_text()
		info_list_tmp = info_str.split("\n")[1:-1]
		ret_list.append(info_list_tmp)
	return ret_list

if __name__ == "__main__":
	list_tmp = get_data(url_2)
	ret = get_info_list(list_tmp)
	for i in ret:
		print(i)
