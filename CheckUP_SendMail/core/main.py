#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

import os
import sys
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import checkUp
import sendMail
import mylogging

logger = logging.getLogger(__name__)


def run():
	users_dic = checkUp.get_users_dic()
	# 遍历字典发送提醒邮件
	for user in users_dic:
		tmp_list = []
		for item in users_dic[user]:
			if item:
				tmp_list.append("ip: {:<20} - 宿主机: {:<20}<br>".format(item.get("ip"), item.get("master", "未定义")))
			else:
				logger.info("users_dic[{}] is none!".format(user))
		logger.debug("user:{},ip_list:{}".format(user, tmp_list))
		if len(tmp_list) > 0:
			sendMail.send_mail(tmp_list, user)  # 没有配置user的主机默认将邮件发给白晓
		else:
			logger.info("Can't find any hosts under user:{}".format(user))

if __name__ == "__main__":
	run()
