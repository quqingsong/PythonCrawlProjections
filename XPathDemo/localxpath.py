#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :localxpath.py
# @Time      :2020/5/9 23:24
# @Author    :青松
 
from lxml import etree

def readdata():
    filepath = r"D:\PycharmProjects\kuaidaili\国内高匿免费HTTP代理IP - 快代理.html"
    # filepath2 = r"D:\PycharmProjects\kuaidaili\1.txt"
    with open(filepath, "rb") as f:
        # print(f.read())
        data=f.read()
        print(data)
        return data

def anaysisdata(data):
    mytree=etree.HTML(data)
    mydata=mytree.xpath("//*[@id=\"list\"]/table/tbody/tr[1]/td[5]/text()")[0]
    print(mydata)

if __name__=="__main__":
    data=readdata()
    anaysisdata(data)
