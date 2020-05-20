#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :pyqueryfirstpage.py
# @Time      :2020/5/9 21:19
# @Author    :青松
 

from pyquery import PyQuery as py
from lxml import etree

def readdata():
    filepath = r"D:\PycharmProjects\kuaidaili\国内高匿免费HTTP代理IP - 快代理.html"
    #读入的是二进制数据流
    with open(filepath, "rb") as f:
        # print(f.read())
        data=f.read()
        return data

def anaysisdata(data):
    doc=py(data)
    item=doc("title").text()
    print(item)

if __name__=="__main__":
    data=readdata()
    anaysisdata(data)