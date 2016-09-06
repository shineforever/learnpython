from django.shortcuts import render, HttpResponse
import json

# Create your views here.

# 假装DB
db = {
    "Alex": {
        "name": "Alex",
        "age": 18,
    },
    "Bob": {
        "name": "Bob",
        "age": 22,
    },
    "Jack": {
        "name": "Jack",
        "age": 23,
    }
}


def demo3(request, db_name, user_name, check_what, callback_name):
    print(db_name, user_name, check_what, callback_name)  # 打印下client端通过url传来的参数
    ret = db.get(user_name).get(check_what)  # 根据client端传来的参数去数据库查询相关信息
    ret_data = {"data": ret}  # 将结果放到一个字典里，key一般设为data
    print(ret_data)
    # jsonp最重要的部分，用client告诉你的callback函数把数据包起来，组成字符串返回
    ret_str = callback_name + "(" + json.dumps(ret_data) + ")"
    return HttpResponse(ret_str)  # 返回结果
