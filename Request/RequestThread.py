#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Request.py
# @Time      :2020/4/24 20:03
# @Author    :青松

import requests
from lxml import etree
import time
import gevent.monkey
import os
import threading
import multiprocessing


# 首页网页
url = 'https://www.kuaidaili.com/free/inha/'


def gethtmllink(url):
    headers = {'Host': 'example.com',
               'Connection': 'keep-alive',
               'Cache-Control': 'max-age=0',
               'Accept': 'text/html, */*; q=0.01',
               'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
               'DNT': '1',
               'Referer': 'http://example.com/',
               'Accept-Encoding': 'gzip, deflate, sdch',
               'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'
               }
    proxies = {
        "http": "203.76.240.133:24754",
        "https": "203.76.240.133:24754"

    }
    response = requests.get(url,headers=headers)
    html = response.text
    mytree = etree.HTML(html)
    table = mytree.xpath('//table[@class="table table-bordered table-striped"]//th/text()')
    print(format(table[0], '<17'), format(table[1], '<7'), format(table[2], '<6'), format(table[3], '<5'),
          format(table[4], '<45'), format(table[5], '<8'), format(table[6], '<20'))
    pagecount = mytree.xpath('//div[@id="listnav"]//li[last()-1]/a/text()')[0]
    # print(pagecount)
    urlfirst = 'https://www.kuaidaili.com/free/inha/'
    urllist = []
    for i in range(1, 300 + 1):
        urllist.append(urlfirst + str(i) + '/')
    # for i in urllist:
    #     print(i)
    return urllist


# 多级网页解析
def gethtml(url):
    headers = {'Host': 'example.com',
               'Connection': 'keep-alive',
               'Cache-Control': 'max-age=0',
               'Accept': 'text/html, */*; q=0.01',
               'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
               'DNT': '1',
               'Referer': 'http://example.com/',
               'Accept-Encoding': 'gzip, deflate, sdch',
               'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'
               }
    proxies = {
        "http": "203.76.240.135:5207",
        "https": "203.76.240.135:5207"
    }
    print(url)
    print("进程ID:", os.getpid())
    response = requests.get(url, headers=headers,proxies=proxies)
    html = response.text
    mytree = etree.HTML(html)
    # ip地址
    ip = mytree.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[1]/text()')
    # 端口号
    prop = mytree.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[2]/text()')
    # 匿名度
    anonymity = mytree.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[3]/text()')
    # 类型
    types = mytree.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[4]/text()')
    # 位置
    location = mytree.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[5]/text()')
    # 响应速度
    speed = mytree.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[6]/text()')
    # 最后验证时间
    lasttime = mytree.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[7]/text()')
    myfile='快代理.txt'
    # if os.path.exists(myfile):
    #     os.remove(myfile)
    # else:
    time.sleep(2)
    savefile = open(myfile, 'a')

    savefilelist=[]
    for i in range(0, 15):
        print(format(ip[i], '<17'), format(prop[i], '<7'), format(anonymity[i], ' <6'), format(types[i], ' <7'),
              format(location[i], '<40'), format(speed[i], '<10'), format(lasttime[i], '<2'), )
        savefilelist=format(ip[i], '<17')+format(prop[i], '<7')+format(anonymity[i], ' <6')+format(types[i], ' <7')+format(location[i], '<40')+format(speed[i], '<10')+format(lasttime[i], '<2')
        savefile.writelines(savefilelist+'\n')
    savefile.close()


if __name__ == '__main__':
    urllist=gethtmllink(url)
    start=time.time()
    threadlist=[]
    pool=multiprocessing.Pool(processes=3)
    for urls in urllist:
        # print(urls)
        #元组中只包含一个元素时，需要在元素后面添加逗号，args=(urls,)
        #这里开启线程
        # mythread=threading.Thread(target=gethtml,args=(urls,))
        # mythread.start()
        # threadlist.append(mythread)
        pool.apply_async(gethtml,(urls,))
    pool.close()
    pool.join()
    end=time.time()

    # for thd in threadlist:
    #     thd.join()
    # end=time.time()
    print("运行的时间为:",end-start)