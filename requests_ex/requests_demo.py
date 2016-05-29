#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
requests的练习
"""

import requests
import urllib.parse

LAGOU_GATEWAY = 'http://www.lagou.com/jobs/positionAjax.json?'
sess = requests.Session()
kd = 'Python'
params = {'city': '北京', 'gx': '全职', 'yx': '21k-50k'}
page = 1
url_encoded = urllib.parse.urlencode(params)
jl_url = LAGOU_GATEWAY + url_encoded
print(jl_url)
payload = {
	'first': False,
	'pn': page,
	'kd': kd
}
r = sess.post(jl_url, data=payload)
json_result = r.json()
# print(json_result['content'])
print(type(json_result['content']))
# print(json_result['content']['positionResult']['result'])
# for i in json_result['content']['positionResult']['result']:
	# print(i['companyName'])
	# print(i)

# job_demo = json_result['content']['positionResult']['result'][0]
# for k in job_demo:
# 	print(k, job_demo[k])
for k in json_result['content']['positionResult']:
	print(k)

print(json_result['content']['positionResult']['totalCount'])
# print(json_result['content']['positionResult']['totalPageCount'])
