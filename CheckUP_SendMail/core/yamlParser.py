#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
解析虚拟机列表的配置文件，得到所有的虚拟机信息
"""

import yaml
import os
import sys
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

logger = logging.getLogger(__name__)


# 解析存放虚拟机列表的yml文件
def yml_parser(yml_file):
	with open(yml_file) as f:
		info_dic = yaml.load(f)
		return info_dic
