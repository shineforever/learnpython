#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

import time
import datetime
import yaml
import os
import logging

logger = logging.getLogger(__file__)


conf_file = "D:\\WorkSpace\\learnpython\\HomeworkCheck\\conf\\check_setting.yaml"

t1 = datetime.datetime.today().date()  # 获取到运行当天的时间
print(t1)
print(type(t1))

t2 = "2016-07-22"  # 配置文件中配置的时间
print(t2)
print(type(t2))
t3 = datetime.datetime.strptime(t2, "%Y-%m-%d").date()
print(t3)
print(type(t3))
date_delta = t1 - t3

print(date_delta.days // 7 + 1)

week_today = datetime.datetime.today().strftime("%u")
print(type(week_today))


def check_do():
    """
    系统级定时任务启动该函数以后，该函数去判断是否有需要执行作业检查
    其实也就是找出周六去检查哪些，周日去检查哪些
    :return:返回此次要去检查的目录相关信息
    """
    global conf_data
    try:
        with open(conf_file, encoding="utf8") as f:
            conf_data = yaml.load(f)
    except Exception as e:
        logger.error("invalid config file. Error:{}".format(str(e, encoding="utf8")))
        exit()
    day_of_the_week = int(datetime.datetime.today().strftime("%u"))  # 今天是这个周的第几天
    ret_data = conf_data.get(day_of_the_week, None)  # 去配置文件中找今天要检查的目录
    logger.info("load conf file success.")
    return ret_data


def check_homework(arg_dic):
    """
    遍历目录，检查作业是否交
    :return:
    """
    for record_temp in arg_dic:
        semester = record_temp  # 学期号
        check_path = arg_dic[record_temp].get("dir_path", None)  # 待检查的目录
        # TODO 遍历目录下所有的文件夹，往下第一层是每个人的文件夹(文件夹名是学号)
        # TODO 目标是得到每个人文件夹下最新的文件夹，返回文件名和文件总大小
        # TODO 按本周有没有提交来分类？
        os.walk()
        pass
