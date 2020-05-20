#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :RegularExpressionDemo.py
# @Time      :2020/3/24 14:16
# @Author    :青松

'''
        re.S 使 ． 匹配包括换行在内的所有字符

'''
import requests
import re

response=requests.get('http://quotes.toscrape.com/')
text=response.text

str2='<div.*<a href="/" style="text-decoration: none">(.*)</a>.*</h1>'
str3=re.findall(str2,text,re.S)
print(str3[0])