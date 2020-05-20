#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :readfileDemo.py
# @Time      :2020/4/14 17:56
# @Author    :青松

from lxml import etree
import re

def readfile():
    filepath='html.txt'
    readfile=open(filepath,'r',encoding='UTF-8')
    mylist=readfile.read()
    # print(mylist)
    return mylist

def xpath(file):
    mytree=etree.HTML(file)
    #data=mytree.xpath("//*[@class=\"dxypage clearfix\"]/text()")
    data=mytree.xpath("//*[@id=\"article\"]/div[3]/div[2]/text()")[0]
    print(data)
    str= '页次：1/(.*) 每页'
    page=re.findall(str,data,re.S)
    print(page[0])

if __name__=='__main__':
    file=readfile()
    xpath(file)


