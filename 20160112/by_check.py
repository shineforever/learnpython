#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
白宇的代码
"""

flag = False                                       # 设置标志位,用户退出
budget = int(input("请输入您的购物预算:"))           # 用户预算金额
balance = int(budget)                               # 余额
while not flag:
    print('欢迎购物'.rjust(30,' '))
    print(33*' ','余额:',balance)
    print(' '*15,'#'*30)
    print(' '*15,'1)',' '*1,'tee',' '*15,'200')
    print(' '*15,'2)',' '*1,'iphone6s',' '*10,'5999')
    print(' '*15,'3)',' '*1,'fenix3',' '*12,'999')
    goods = {
        1:['tee','200'],
        2:['iphone6s','5999'],
        3:['fenix3','999']
    }
    user_choose_number = int(input('请输入商品编号(输入0退出):'))
    if user_choose_number == 0:
        print(' '*15, '此次消费:', budget - balance, '余额:', balance)
        flag = True
    if user_choose_number in goods.keys():
        if balance >= int(goods[user_choose_number][1]):
            balance = int(balance - int(goods[user_choose_number][1]))
            print(' '*15,'余额:', balance)
        else:
            print(' '*15,'余额不足')
            print(' '*15,'余额:', balance)

    else:
        print(' '*15, '没有此商品')
        print(' '*15, '余额:', balance)
