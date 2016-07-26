#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

gouwuShop = {
	'prdList': {
		'iphone5': 2000,
		'iphone6': 3500,
		'iphone6s': 4000,
		'牙膏': 15,
		'电风扇': 99
	},
	'spCart': [

	]
}


def serialize():
	keysList = list(gouwuShop['prdList'].keys())
	sortKeys = sorted(keysList)
	return sortKeys

