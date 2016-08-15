#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

import time
import datetime
import yaml
import os
import logging
from collections import defaultdict

logger = logging.getLogger(__name__)


conf_file = "D:\\WorkSpace\\learnpython\\HomeworkCheck\\conf\\check_setting.yaml"


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
        # TODO 我突然有了一个好idea,bla....
        os.walk()
        pass


def get_dir_list(file_path):
    """
    获取指定目录下的文件夹列表
    :param file_path: 要去遍历的路径
    :return:
    """
    dir_list = []
    file_list = os.listdir(file_path)  # 先获取目录下所有的文件列表
    for i in file_list:  # 便利找出所有的文件夹
        path_tmp = os.path.join(file_path, i)
        if os.path.isdir(path_tmp):
            dir_list.append(path_tmp)
    return dir_list


def check_commit(dir_list):
    """
    检查是否有交作业
    以学生目录有没有在本周进行过修改为判断依据
    :param dir_list: 学生作业文件夹 的列表
    :return: 返回一个字典
    """
    ret_dic = defaultdict(list)
    today = datetime.date.today()
    week_today = today.weekday()
    date_delta = datetime.timedelta(days=week_today)
    this_monday = today - date_delta  # 本周一
    this_monday_stamp = time.mktime(this_monday.timetuple())  # 本周一的时间戳
    for i in dir_list:
        stat_info = os.stat(i)  # 获取文件信息
        last_modify_time = stat_info.st_mtime  # 文件最后修改时间
        stu_num = os.path.split(i)[1]  # 学号
        if last_modify_time > this_monday_stamp:  # 本周有修改
            ret_dic["yes"].append(stu_num)  # 交了作业
        else:
            ret_dic["no"].append(stu_num)  # 没交作业
    return ret_dic


def get_homework_info(stu_list):
    """
    获取提交作业的学生最近更新的文件夹的文件详情
    :param stu_list: 交作业的学号 列表
    :return: 学号: 作业详情
    """
    for i in stu_list:
        stu_path = os.path.join()
