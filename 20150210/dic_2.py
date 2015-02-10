#!/usr/bin/env python
# -*- coding:utf8 -*-


contact_dic = {}
with open('contact_list.txt') as f:
	for i in f.readlines():
		line = i.strip().split()
		contact_dic[line[0]] = line[1:]

print contact_dic
