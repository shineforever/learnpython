__author__ = "Feng Guofu"
import re

'''
正则表示：
    匹配数字（负数、小数）： \-?\d+\.?\d+
'''
# Regular expressions
# 数值（正数负数、整数小数）
regex_num = '\-?\d+(\.\d+)?'
# 匹配出公式中的负号数值，包含负号前的运算符或括号“（”
regex_minus = '((^\-)|(\D\-))?\d+(\.\d+)?'
# regex_minus = '[(^\-)(\D\-)]?\d+(\.\d+)?'  【】这样用，匹配有问题中间的小括号并不是整体


def add(x, y, c_type):
    '''
    加减法运算
    :param x: 第一个运算值
    :param y: 第二个运算值
    :param type: 运算类型
	:return num: 运算结果
    '''
    num = 0
    if c_type == '+':
        num = float(x) + float(y)
    elif c_type == '-':
        num = float(x) - float(y)
    return num


def multi(m, n, c_type):
    '''
    乘除法运算
    :param m: 第一个运算值
    :param n: 第二个运算值
    :param type: 运算类型
	:return num: 运算结果
    '''
    num = 0
    if c_type == '*':
        num = float(m) * float(n)
    elif c_type == '/':
        num = float(m) / float(n)
    return num


def counts(operation):
    '''
    判断公式中有几个数值
    :param operation: 运算式
	:return count: 数值个数
    '''
    # 判断公式中第一个值是不是负数
    result_tmp = re.match('\-',operation)
    if result_tmp is not None:
        # 去除公式中第一个值的负号
        result_tmp = re.sub('\-','',operation,1)
        count = re.compile('[\+\-\*\/]').split(result_tmp)
    else :
        count = re.compile('[\+\-\*\/]').split(operation)
    return count


def parentheses(operation):
    '''
    括号处理，取出最内部括号里的运算式
    :param operation: 运算式
	:return :
    '''
    # 匹配括号内只有数字或‘+-*/’的部分
    print("\33[31m计算公式为：\n %s \33[0m" %operation)
    result_src = re.search('\([0-9\+\-\*\/]+\)',operation)
    if result_src is not None:
        print("当前处理的括号内result_src公式：",result_src.group())
        # 去除取出部分的括号
        result = re.sub('\(|\)', '', result_src.group())
        print("去除括号后的result公式：",result)
        count = counts(result)
        # 判断是否只是一个数字（包括负数和浮点数）
        if len(count) == 1:  # 是数字则替换掉原公式
            # 原公式替换
            operation = operation.replace(result_src.group(),result,1)
            print("此次数值内单括号处理完成\n",operation)
        else: # 是公式，交给calculate函数处理
            print("开始括号内公式处理：",result)
            # 调用calculate处理公式
            result = calculate(result)
            # 对于返回结果替换原公式
            print(result)
            input('')
            operation = operation.replace(result_src.group(), str(result),1)
            # 递归调用
            parentheses(operation)
    else:
        calculate(operation)


def calculate(operation):
    '''
    乘除加减运算，计算出没有括号部分公式的结果。调用add、multi函数
    :param operation: 运算式
	:return :
    '''

    # 匹配出乘法和除法（包含有负数和负数没有括号的情况）
    mul_div = re.search(regex_minus+'[\*\/]'+regex_num,operation)
    # 匹配出加法和减法
    add_sub = re.search(regex_minus+'[\+\-]'+regex_num,operation)
    # 乘除法处理
    if mul_div is not None:
        # 取出运算类型
        print("当前计算公式：",mul_div.group())
        c_type = re.search('\*|\/', mul_div.group()).group()
        # 以运算类型作为分隔符
        p = re.compile('[\*\/]')
        # 获取到运算的两个值
        nums = p.split(mul_div.group())
        # 计算运算结果
        result = multi(nums[0], nums[1], c_type)
        # 把计算公式替换成计算结果
        operation = operation.replace(mul_div.group(),str(result),1)
        print("乘除法计算后运算结果：", operation)

    # 加减法处理
    # -1-2  -1+2  -1--2  -1+-2  1-2  1+2  1--2  1+-2
    elif add_sub is not None:
        result = add_sub.group()
        # 查看有无“--”算法(-1--2  1--2)
        minus_two = re.search('\-\-', result)
        if minus_two is not None:
            result.replace('--', '+',1)
        # 查看有无“+-”算法(-1+-2  1+-2)
        plus_minus = re.search('\+\-', result)
        if plus_minus is not None:
            result.replace('+-', '-',1)

        # 负数减正数的情况(-1-2)
        negative2 = re.match('\-\d+(\.\d+)?\-\d+(\.\d+)?',result)
        if negative2 is not None:
            nums = re.compile('\-').split(result)  # 列表三个元素
            results = add(0-float(nums[1]), 0-float(nums[2]), '+')
        # 负数加正数的情况(-1+2  1+2)
        negative1 = re.match('\-?\d+(\.\d+)?\+\d+(\.\d+)?',result)
        if negative1 is not None:
            nums = re.compile('\+').split(result)
            results = add(0-float(nums[0]), 0-float(nums[1]), '+')
        # 正数减正数的情况(1-2)
        minus = re.match('\d+(\.\d+)?\-\d+(\.\d+)?', result)
        if minus is not None :
            nums = re.compile('\-').split(result)
            results = add(nums[0], nums[1], '-')

        print('此次加减法运算结果：',results)
        operation = operation.replace(add_sub.group(),str(results),1)
        print("加减法法计算后运算结果：", operation)

    count = counts(operation)
    print("次数",len(count))
    # 如果公式数值个数大于1，继续处理
    if len(count) > 1:
        calculate(operation)
    else:
        print("\33[31m括号内运算部分完成\n %s\33[0m" %operation)
        return operation


# parentheses("(-40*5-2/3)+(-40/5)")  # 加上非个位数，两位或多位数的情况

# a = calculate('1-2+2*3/5')
a = calculate('1-2+2')
print('===============================',a)

