#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
从配置的所有主机中找出还在开机的虚拟机
暂且使用ping的方式判断虚拟机是否开机？
"""

import os
import sys
import subprocess
import re
import logging
from collections import defaultdict
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import yamlParser
from conf import settings

logger = logging.getLogger(__name__)


def check_host(ip_list):
	up_ip_list = []
	for ip in ip_list:
		ping_cmd = "ping -c 1 {}".format(ip)
		p = subprocess.Popen(ping_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		out_info = p.stdout.read().decode()
		logger.debug(out_info)
		re_p = re.compile(r'time=\d*', re.IGNORECASE | re.MULTILINE)
		logger.debug(re_p)
		if len(re_p.findall(out_info)) > 0:
			logger.debug("{}:UP!".format(ip))
			up_ip_list.append(ip)
		else:
			logger.debug("{}:DOWN!".format(ip))
		logger.debug("up主机数:".format(len(up_ip_list)))
		logger.debug(up_ip_list)
	return up_ip_list


def get_up_hosts():
	hosts_dic = yamlParser.yml_parser(settings.CONFFILE)  # 得到配置文件文件中的主机信息
	ip_list = check_host(list(hosts_dic.keys()))  # 找到所有能ping通的IP
	up_hosts_dic = {}
	if len(ip_list) > 0:
		for ip in ip_list:
			if ip:
				logger.debug(ip)
				logger.debug(hosts_dic.get(ip))
				up_hosts_dic[ip] = hosts_dic.get(ip)
	else:
		logger.info("No hosts up!")
	return up_hosts_dic


# 按照user将IP分组，即一个人可以分管多个IP
def get_users_dic():
	up_hosts_dic = get_up_hosts()
	logger.debug("up_hosts_dic".format(up_hosts_dic))
	users_dic = defaultdict(list)
	if len(up_hosts_dic) > 0:
		for key in up_hosts_dic:
			# 没有指明user的主机默认发送给baixiao
			if not up_hosts_dic[key]:
				users_dic["baixiao"].append({"ip": key, "master": "未定义"})
			else:
				users_dic[up_hosts_dic[key].get("user", "baixiao")].append({"ip": key, "master": up_hosts_dic[key].get("master", "未定义")})
	logger.debug(users_dic)
	return users_dic
