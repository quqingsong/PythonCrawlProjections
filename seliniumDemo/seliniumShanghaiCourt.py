#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :seliniumShanghaiCourt.py
# @Time      :2020/4/23 23:31
# @Author    :青松
 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import gevent

url='http://www.hshfy.sh.cn/shfy/gweb2017/channel_xw_list.jsp?pa=abG1kbT1MTTAxMDEmbG1tYz23qNS6tq/MrAPdcssPdcssz&zd=xwxx'
def download(url,start,end):
    myoption=Options()
    # myoption.add_argument('--headless')
    brower=webdriver.Chrome(options=myoption)
    brower.get(url)
    gevent.sleep(5)
    for i in range(start,end):
        js="javascript:goPage('"+str(i)+"')"
        brower.execute_script(js)
        print('js is run    '+str(i))
        gevent.sleep(5)


        soup=BeautifulSoup(brower.page_source,'lxml')
        lis = soup.find_all(class_='list_a')
        lists = lis[0].find_all('a')
        for li in lists:
            print(li.text)
        brower.quit()

if __name__=="__main__":
    gevent.spawn(download(url,1,4))
    gevent.spawn(download(url,5,9))
    gevent.spawn(download(url,10,14))
    gevent.spawn(download(url,15,20))

