#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :UniformlyRanking.py
# @Time      :2020/4/17 19:30
# @Author    :青松

from bs4 import BeautifulSoup
from lxml import *
from selenium import webdriver
from  selenium.webdriver.chrome.options import Options

url='http://www.lottery.gov.cn/historykj/history.jspx?_ltype=plw'
def getdata(url):
    myoption=Options()
    # myoption.add_argument('--headless')
    brower=webdriver.Chrome(options=myoption)
    brower.get(url)
    html=brower.page_source
    soup=BeautifulSoup(html,'lxml')
    print(soup.title.string)
    data=soup.find_all(class_="result")
    for line in data[0].find_all('tr'):
        for dat in line.find_all('td'):
            print(dat.string,end='   ')
        print()
    brower.quit()
if __name__=='__main__':
    getdata(url)