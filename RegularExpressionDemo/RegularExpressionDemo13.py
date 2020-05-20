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

response=requests.get('https://www.jb51.net/list/list_97_1.htm')
text=response.text

str2='<div class="dxypage clearfix">(\d+)<a href="#">'
str3=re.findall(str2,text,re.S)
print(str3)