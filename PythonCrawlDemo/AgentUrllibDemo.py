#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :AgentUrllibDemo.py
# @Time      :2020/3/19 18:52
# @Author    :青松



import urllib.request

url='http://www.baidu.com'
def viewUrllibDemo(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
    request=urllib.request.Request(url,headers=headers)
    response=urllib.request.urlopen(url,timeout=10)
    text=response.read().decode('utf-8')
    print(text)

viewUrllibDemo(url)