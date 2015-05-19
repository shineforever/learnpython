#!/usr/bin/env python
# -*- coding:utf8 -*-

import difflib
import sys

try:
    textfile1 = sys.argv[1]    #第一个配置文件路径参数
    textfile2 = sys.argv[2]    #第二个配置文件路径参数
except Exception,e:
    print "Error:"+str(e)
    print "Usage:simple3.py filename1 filename2"
    sys.exit()

def readfile(filename):    #文件读取分隔函数
    try:
        fileHandle = open(filename,'rd')
        text = fileHandle.read().splitlines()    #读取后，以行进行分隔
        fileHandle.close()
        return text
    except IOError as error:
        print ('Read file Error:'+str(error))
        sys.exit()

if textfile1 == "" or textfile2 == "":
    print "Usage simple3.py filename1 filename2"
    sys.exit()

text1_lines = readfile(textfile1)    #调用readfile函数，获取分隔后的字符串
text2_lines = readfile(textfile2)

d = difflib.HtmlDiff()    #创建HtmlDiff()类对象
print d.make_file(text1_lines,text2_lines)
