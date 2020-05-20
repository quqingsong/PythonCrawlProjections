#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :UrllibDemo.py
# @Time      :2020/3/19 14:36
# @Author    :青松


import urllib.request

url='http://www.baidu.com'
def viewCode(url):
    response=urllib.request.urlopen(url,timeout=10)
    # print(response.info())
    print(response.read())#读取网页源代码
text=viewCode(url)
print(text)
