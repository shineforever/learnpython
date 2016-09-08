#!/usr/bin/env python
# _*_coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup
#from tkinter import *
import xlwt3
#import xlrd
#import xlwt
import datetime,time
from tkinter import *
from tkinter import messagebox
# https://www.baidu.com/s?wd=%E7%A8%8B%E5%BA%8F%E5%91%98&ie=utf-8&pn=20
base_url = "https://www.baidu.com/s?wd="
keywords = ""
page_url = "&ie=utf-8&pn="
linkhref = ""
data = []
list = []
#hea是我们自己构造的一个字典，里面保存了user-agent。  
#让目标网站误以为本程序是浏览器，并非爬虫。  
#从网站的Requests Header中获取。【审查元素】  
hea = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}  
#page_num = input("plz enter the page:")

root = Tk()
root.title("searchTool")
root.geometry('300x300')  # 是x 不是*

#文本框输入需要的页数何关键字
l1 = Label(root, text="页数：")
l1.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
page_text = StringVar()
xls = Entry(root,textvariable=page_text)
page_text.set("")
xls.pack()

l2 = Label(root, text="关键字：")
l2.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
keywords_text = StringVar()
sheet = Entry(root,textvariable=keywords_text)
keywords_text.set(" ")
sheet.pack()

#存储数据到excel
wb=xlwt3.Workbook()
sheet=wb.add_sheet("sheet_test",cell_overwrite_ok=False)
#keywordsinput = input("plz enter your keywords:")

nowtiem = time.strftime("%Y%m%d%H%M%S")

def on_click(*args):
    pageget = page_text.get()
    keywords = keywords_text.get()
    print(pageget,keywords)
    string = str("page：%s keywords：%s " % (pageget, keywords))
    #string = str(pageget)
    #print(string)
    print("page：%s keywords：%s " % (pageget, keywords))
    messagebox.showinfo(title='aaa', message=string)

    def trade_spider(max_pages):
        page = 0
        while page < max_pages:
            url = base_url + keywords + page_url + str(page * 10)  # 控制第几页
            print(url)
            print("----------------------------------------------------")
            source_code = requests.get(url, headers=hea)
            # print(source_code)
            plain_text = source_code.text
            print(plain_text + "plaintest")
            soup = BeautifulSoup(plain_text, "html.parser")
            for div in soup.findAll('div', {'class': "result c-container "}):
                # print ("---------for start-----------,over")
                link = div.find('a')
                linktext = (link.text)  # 标题
                if div.find("div", {"class": "c-abstract"}):
                    content = div.find("div", {"class": "c-abstract"}).text  # 描述
                elif div.find("div", {"class": "c-span18 c-span-last"}):
                    content = div.find("div", {"class": "c-span18 c-span-last"}).text
                if div.find("div", {"class": "c-showurl"}):
                    reallink = div.find("div", {"class": "c-showurl"}).text  # 描述
                elif div.find("div", {"class": "g"}):
                    reallink = div.find("div", {"class": "g"}).text
                elif div.find("div", {"class": "f13"}):
                    reallink = div.find("div", {"class": "f13"}).text
                # reallink = div.find("a", {"class": "c-showurl"}).text #副链接
                # print("print reallink:")
                # print(reallink)
                # print(content)
                linkhref = (link.get('href'))  # 链接
                data = [linktext, linkhref, str(content), reallink]
                # print(data)
                list.append(data)
            page += 1

        for i in range(0, len(list)):
            for j in range(len(list[i])):
                sheet.write(i, j, list[i][j])
            wb.save(keywords + "_" + nowtiem + ".xls")

            # print(data)

    keywords = keywords_text
    #trade_spider(pageget)  # 控制总共需要的页数
    trade_spider(int(pageget))



#sheet.bind('<Return>', on_click)
#xls.bind('<Return>', on_click)

Button(root, text="start",command=on_click).pack()
root.mainloop()


