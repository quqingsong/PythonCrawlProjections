#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :seleniumjb51.py
# @Time      :2020/4/13 21:32
# @Author    :青松

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
import re

url = 'https://www.jb51.net/list/list_97_1.htm'


# 获取当前首页网页，方便提取数据
def geturl(url):
    # 网页url
    myoption = Options()
    # 无窗口界面
    myoption.add_argument('--headless')
    browser = webdriver.Chrome(options=myoption)
    # 浏览器读取网页数据
    browser.get(url)
    # print(browser.page_source)
    # 网页标题
    data = browser.page_source
    return data


# 读取网页页码
def geturlpage(data):
    # print(data)
    mytree = etree.HTML(data)
    # 网页指定数据,xpath返回的是list
    text = mytree.xpath("//*[@id=\"article\"]/div[3]/div[2]/text()")[0]
    str2 = '页次：1/(.*) 每页'
    # findall返回list
    page = re.findall(str2, text, re.S)[0]
    # print(page)
    number = eval(page)
    # print(number)
    # print(type(number))
    # urllist网址
    urllist = []
    # get网页解析成功
    for i in range(1, number + 1):
        urllist.append('https://www.jb51.net/list/list_97_' + str(i) + '.htm')
    # print(urllist)
    return urllist


# 解析每页的tittle
def gettittle(urlpage):
    myoption = Options()
    myoption.add_argument('--headless')
    brower = webdriver.Chrome(options=myoption)
    brower.get(urlpage)
    data = brower.page_source
    # print(data)
    mytree = etree.HTML(data)
    # tittles=mytree.xpath('//*[@id="article"]/div[3]/dl/dt/a/@href')
    # //*[@id="article"]/div[3]/dl/dt[1]/a
    # //*[@id="article"]/div[2]/dl/dt[1]/a
    # tittles=mytree.xpath('//*[@id="article"]/div[2]/dl/dt/a/@title')
    #//*[@id="article"]/div[3]/dl/dt[1]/a
    tittles = mytree.xpath('//*[@class="artlist clearfix"]/dl/dt/a/text()')
    # tittles = mytree.xpath('//*[@id="article"]/div[2]/dl/dt/a/text()')  #成功

    print(tittles)
    print(len(tittles))
    # savefile=open('tittle.txt','w')
    # for tittle in tittles:
    #     savefile.readlines(tittle)
    # for tittle in tittles:
    #     print(tittle)


if __name__ == '__main__':
    data = geturl(url)
    urllist = geturlpage(data)
    # print(urllist)
    gettittle('https://www.jb51.net/list/list_97_2.htm')

    # for url in urllist:
    # print(url)



