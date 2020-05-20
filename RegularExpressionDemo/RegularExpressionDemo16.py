#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :RegularExpressionDemo.py
# @Time      :2020/3/24 14:16
# @Author    :青松

'''
        re.S 使 ． 匹配包括换行在内的所有字符

'''
import re
import urllib.request
text='''
页次：1/513 每页40 文章数20513  
'''

# str2='<a.*?>(.*)</a>'
str2='页次：1/(.*)每页'
str3=re.findall(str2,text,re.S)
if str3:
    print(str3[0])
    # print(str3[0])
else:
    print('没有')
