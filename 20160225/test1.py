#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
有序字典的练习
"""
from collections import OrderedDict

GOODS_TYPE = {
    "eat": {
        "六元麻辣烫": {"price": 6, "power_amount": 1},
        "庆丰包子": {"price": 36, "power_amount": 5},
        "金钱豹自助餐": {"price": 238, "power_amount": 10}
    },
    "work": {
        "餐馆服务员": {"pay": 1, "power_amount": 20},
        "IT公司运维": {"pay": 10, "power_amount": 15},
        "金融公司开发": {"pay": 30, "power_amount": 10},
    },
    "learn": {
        "PHP": {"price": 5000, "ability_amount": 2},
        "JAVA": {"price": 8000, "ability_amount": 5},
        "Python": {"price": 10000, "ability_amount": 10}
    },
    "consume": {
        "奇瑞QQ": {"price": 30000, "confidence_amount": 10},
        "哈弗H6": {"price": 150000, "confidence_amount": 30},
        "特斯拉P90D": {"price": 1000000, "confidence_amount": 100},
        "三环大房子": {"price": 20000000, "confidence_amount": 2000},
    },
}

d1 = OrderedDict()
d = GOODS_TYPE["eat"]
# for k, v in enumerate(GOODS_TYPE["eat"], 1):
# for k, v in enumerate(d, 1):
# 	# print(k, v)
# 	d1[k] = v
# for key in d1:
# 	print(key, d1[key])

menu_dic = GOODS_TYPE["eat"]
option_dic = OrderedDict()
for k, v in enumerate(menu_dic, 1):
    option_dic[k] = v
print("食品目录：")
for key in option_dic:
    print("{}: {}".format(key, option_dic[key]))
while True:
    option = input("==>").strip()
    print(option)
    print(option_dic.keys())
    print(1 in option_dic.keys())
    print(int(option) in option_dic.keys())
    if int(option) in option_dic.keys():
        print("吃着呢。。。")
    else:
        print("没这一项。。。")


