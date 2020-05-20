#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :sunpoliticsdetail.py
# @Time      :2020/5/18 0:12
# @Author    :青松

import requests
from lxml import etree
import time
import gevent.monkey
import os


# 首页网页
url = 'http://wz.sun0769.com/political/politics/index?id=456614'


#读取文件
def readfile():
    filepath="sunpoliticsdetail.html"
    with open(filepath,"rb") as file:
        html=file.read().decode("utf-8")
        # print(html)
    return html
# 多级网页解析
def gethtml(url):
    headers = {
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    #     "Accept-Encoding":"gzip, deflate",
    #     "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    #     "Cache-Control": "max-age=0",
    #     "Connection":"keep-alive",
    #     "Host":"wz.sun0769.com",
    #     "Referer":"http://wz.sun0769.com/political/index/politicsNewest?id=1&page=4",
    #     "Upgrade-Insecure-Requests": "1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72",
               }
    cookie={
        "amplitude_id_476d446d2d57aa9a7764732a26466a97sun0769.com": "eyJkZXZpY2VJZCI6ImUzOTM5MDllLWE0ZjMtNGY4MC04ZmVjLWZmZjJjZTZjZDZiNlIiLCJ1c2VySWQiOiI4NTJhN2RlMy0xM2E3LTRhOTUtOGJmZC0xZDVmYjFkYTJiZjQiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE1ODc4MTc0NDAzNzUsImxhc3RFdmVudFRpbWUiOjE1ODc4MTc0NDAzNzYsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjgsInNlcXVlbmNlTnVtYmVyIjo4fQ==;",
        " PHPSESSID": "ke7celrvo6rr10d9ebase6l15l;",
        "Hm_lvt_3ac08b9ee936f8dd8b720065d8af23d0": "1589619454,1589682994;",
        "Hm_lpvt_3ac08b9ee936f8dd8b720065d8af23d0": "1589763680"
    }
    proxies = {
        "http": "203.76.240.135:14251",
        "https": "203.76.240.135:14251"
    }
    #,proxies=proxies
    response = requests.get(url,headers=headers)
    html=response.text
    # html = readfile()
    # print(html)
    mytree = etree.HTML(html)
    #可以读取数据
    # titles=mytree.xpath("/html/body/div[3]/div[2]/div[2]/p/text()")[0]
    # print(titles)
    # titles=mytree.xpath("//div[@class=\"focus-date clear focus-date-list\"]/span [4]/text()")
    #不行
    titles=mytree.xpath("//div[@class=\"focus-date clear focus-date-list\"]/span [@class=\"f1\"]/text()")
    # print(titles)
    listlis=mytree.xpath('//div[@class="mr-three"]')
    # print(len(listlis))
    # print(listlis)
    for li in listlis:
        # print(li)
        # 编号
        id = li.xpath('normalize-space(./div [@class="focus-date clear focus-date-list"]/span[4]/text())')
        print(id)
        # print(len(id))
        # 标题
        title = li.xpath('normalize-space(./p/text())')
        print(title)
        # 发布人
        # person = li.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/span[1]/text()')
        # print(person)
        # 发布时间
        issuetime = li.xpath('normalize-space(.//span[2]/text())')
        print(issuetime)
        # 发布内容
        issuecontent = li.xpath('normalize-space(./div[@class="details-box"]/pre/text())')
        print(issuecontent)
        # 处理状态
        dealstate = li.xpath('normalize-space(.//span[3]/text())')
        print(dealstate)
        # savefilelist=id+"\t"+title+"\t"+person+"\t"+issuetime+"\t"+issuecontent+"\t\t"+dealstate

if __name__ == '__main__':
    start=time.time()
    gethtml(url)

    end=time.time()
print("运行时间为:",end-start)