#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :BS4.py
# @Time      :2020/4/16 20:25
# @Author    :青松


from bs4 import BeautifulSoup
from lxml import etree
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import re

url='https://www.jb51.net/list/list_97_1.htm'


def geturl(url):
    myoption = Options()
    myoption.add_argument('--headless')
    brower = webdriver.Chrome(options=myoption)
    brower.get('https://www.jb51.net/list/list_97_1.htm')
    data = brower.page_source
    mytree = etree.HTML(data)
    # 获取页码
    text = mytree.xpath("//*[@id=\"article\"]/div[3]/div[2]/text()")[0]
    str2 = '页次：1/(.*) 每页'
    # findall返回list
    page = re.findall(str2, text, re.S)[0]
    # print(page)
    number = eval(page)
    # 读取网页
    urllist = []
    # get网页解析成功
    for i in range(1, number + 1):
        urllist.append('https://www.jb51.net/list/list_97_' + str(i) + '.htm')
    # print(urllist)
    return urllist

###################################
# 解析数据
def getdata(url):
    myoption = Options()
    myoption.add_argument('--headless')
    brower = webdriver.Chrome(options=myoption)
    brower.get(url)
    html = brower.page_source
    soup=BeautifulSoup(html,'lxml')
    for a in soup.select('dt a'):
        print(a.get_text())
    # # xpath解析
    # mytree = etree.HTML(html)
    # data = mytree.xpath('//*[@class="artlist clearfix"]/dl/dt/a/text()')
    # for list in data:
    #     print(list)
    # savefile = open('html.txt', 'a')
    # for list in data:
    #     savefile.writelines(list + '\n')
    #     print(list)

if __name__ == '__main__':
    myurl = geturl(url)
    # print(myurl)
    for murl in myurl:
        getdata(murl)