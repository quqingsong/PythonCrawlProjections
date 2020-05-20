#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :selenium js读取.py
# @Time      :2020/4/23 17:25
# @Author    :青松
 
from selenium import webdriver
import time
from bs4 import BeautifulSoup

broser=webdriver.Chrome()
broser.get('http://www.hshfy.sh.cn/shfy/gweb2017/channel_xw_list.jsp?pa=abG1kbT1MTTAxMDEmbG1tYz23qNS6tq/MrAPdcssPdcssz&zd=xwxx')
#document.querySelector("#content > div.meneame > div > a:nth-child(3)")
js='document.querySelector("#content > div.meneame > div > a:nth-child(3)")'
# broser.execute_script("javascript:goPage('2')")
# time.sleep(10)
#这种方法不行
# broser.execute_script(js)

# #这种方法可以
# broser.execute_script("javascript:goPage('2')")
# time.sleep(10)
data=broser.page_source
soup=BeautifulSoup(data,'lxml')
# print(soup)
time.sleep(5)
lis=soup.find_all(class_='list_a')
# print(len(ul))
# print(lis[1])
# print(lis[1])
# print(ul)
# a=ul.find('li')
#这里必须用lis[0]
# print(lis[0].find_all('a'))
lists=lis[0].find_all('a')
# print(lists)
# print(len(lists))

for li in lists:
    print(li.text)

# print(data)
broser.quit()