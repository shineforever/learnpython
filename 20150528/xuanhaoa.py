#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

def getResultStr(totalNum,resultNum):
	elements=[x+1 for x in range(totalNum)]
	#将待选的数字添加到elements这个list
	numList=[]
	#创建一个list用于存放选出来的数字
	for i in range(resultNum):
		res=elements[random.randint(0,len(elements)-1)]
		#从list（elements）中随机取数，随机数的范围从0到数列的最后一位
		elements.remove(res)
		#将上一步已经随机选出来的数字从list中去掉，防止造成重复取数
		numList.append(res)
		#将已经选出的数字添加到numList这个list
	numList.sort()
	#将选出来的数字进行排序
	return numList
