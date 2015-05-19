#!/usr/bin/env python
# -*- coding:utf-8 -*-

#求解一元二次方程ax2 + bx + c = 0
import math

def quadratic(a,b,c):
    if not isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
	raise TypeError('参数类型错误')
    else:
	if a ==0 and b!=0:
            return -c/b
        elif a==0 and  b==0:
	    return '参数有异'
	else:
	    m=b**2 - 4*a*c
	    if m>=0:
		print ('返回两个实根')
		return ((-b)+math.sqrt(m))/(2*a),((-b)-math.sqrt(m))/(2*a)
	    else:
		print ('返回两个复根')
		return complex((-b)/(2*a),math.sqrt(m))/(2*a),complex((-b)/(2*a),-math.sqrt(m))/(2*a)
