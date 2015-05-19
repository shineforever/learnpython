#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

def getResultStr(totalCount,resultCount):
	elements = [x+1 for x in range(totalCount)]
	retStr = ''
	for i in range(resultCount):
		res = elements[random.randint(0,len(elements)-1)]
		elements.remove(res)
		retStr += ' '+str(res)
	return retStr
