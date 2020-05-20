#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :sunpolitics.py
# @Time      :2020/5/16 17:04
# @Author    :青松

import requests
from lxml import etree
import time
import gevent.monkey
import os


# 首页网页
url = 'http://wz.sun0769.com/political/index/politicsNewest?id=1&page='

# 多级网页解析
def gethtml(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "wz.sun0769.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72"
               }
    proxies = {
        "http": "203.76.240.135:14251",
        "https": "203.76.240.135:14251"
    }
    #,proxies=proxies
    response = requests.get(url, headers=headers)
    html = response.text
    mytree = etree.HTML(html)
    listlis=mytree.xpath('//span[@class="state3"]//@href')
    print(len(listlis))
    # print(listlis)
    for link in listlis:
        print(link)

def getcoutdata(url,start,end):
    for i in range(start,end+1):
        # url = 'http://wz.sun0769.com/political/index/politicsNewest?id=1&page='
        urlpage=url+str(i)
        gevent.sleep(2)
        print(urlpage)
        gethtml(urlpage)

if __name__ == '__main__':
    start=time.time()
    # gethtml(url)
    gevent.joinall([
        gevent.spawn(getcoutdata,url, 1, 30,),
        gevent.spawn(getcoutdata,url, 31, 60,),
        gevent.spawn(getcoutdata,url, 61, 90,),
        gevent.spawn(getcoutdata,url, 91, 120,),
        gevent.spawn(getcoutdata,url, 121, 150,),
        gevent.spawn(getcoutdata,url, 151, 180,),
        gevent.spawn(getcoutdata,url, 181, 210,),
        gevent.spawn(getcoutdata,url, 211, 240,),
        gevent.spawn(getcoutdata,url, 241, 270,),
        gevent.spawn(getcoutdata,url, 271, 300,)
    ])
    end=time.time()
print("运行时间为:",end-start)