#!/usr/bin/env python
# -*- coding:utf8 -*-

import difflib
text1 = """text1:	#定义字符串1
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""
text1_lines = text1.splitlines()	#以行进行分隔，以便进行对比
text2 = """text2:	#定义字符串2
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""
text2_lines = text2.splitlines()
d = difflib.Differ()	#创建Differ对象
diff = d.compare(text1_lines,text2_lines)	#采用compare方法对字符串进行比较

print '\n'.join(list(diff))
