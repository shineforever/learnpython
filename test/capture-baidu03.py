# coding=utf-8

import urllib2 as url
import string
import urllib
import re
from os.path import exists

def baidu_search(keyword):
    p= {'wd': keyword}
    res=url.urlopen("http://www.baidu.com/s?"+urllib.urlencode(p))
    print res.read()
    # html=res.read()
    # #name = keyword.encode('utf-8')
    # filename = keyword + ".html"
    # htmlresult = open(filename, 'w')
    # htmlresult.write(html)
    # htmlresult.close()
    # return html

def getList(regex,text):
    arr = []
    res = re.findall(regex, text)
    if res:
        for r in res:
            arr.append(r)
    return arr
def getMatch(regex,text):
    res = re.findall(regex, text)
    if res:
        return res[0]
    return ""
def clearTag(text):
    p = re.compile(u'<[^>]+>')
    retval = p.sub("",text)
    return retval

html = baidu_search('music')
# content = unicode(html, 'utf-8','ignore')
#
# arrList = getList(u"<table.*?class=\"result\".*?>.*?<\/a>", content)
#
# for item in arrList:
#     regex = u"<h3.*?class=\"t\".*?><a.*?href=\"(.*?)\".*?>(.*?)<\/a>"
#     link = getMatch(regex,item)
#     url = link[0]
#     title = clearTag(link[1]).encode('utf8')
#     print url
#     print title





