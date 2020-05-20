#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :readsundetail.py
# @Time      :2020/5/18 9:45
# @Author    :青松
 
def readfile():
    filepath="sunpoliticsdetail.html"
    with open(filepath,"rb") as file:
        html=file.readlines()
    print(html)

readfile()
