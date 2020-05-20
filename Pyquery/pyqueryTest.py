#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :pyquery.py
# @Time      :2020/5/8 0:42
# @Author    :青松

from pyquery import PyQuery as py

url = "https://www.kuaidaili.com/free/"


def anaysisepage(url):
    doc = py(url, encoding="utf-8")
    itemss=doc("tr")
    for item in itemss:
        print(item)
        # for dt in item:
        #     print(dt)
        # print(len(item))

    # print(itemss,"\n")

    print("运行完成")

if __name__=="__main__":
    anaysisepage(url)