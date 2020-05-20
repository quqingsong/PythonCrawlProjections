#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :RegularExpressionDemo.py
# @Time      :2020/3/24 14:16
# @Author    :青松

'''
        re.S 使 ． 匹配包括换行在内的所有字符

'''

from bs4 import BeautifulSoup

html='cn.bing.com'
soup = BeautifulSoup(html,'lxml')
print(soup.select('tittle'))
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
