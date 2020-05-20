#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :baidu.py
# @Time      :2020/3/25 20:42
# @Author    :青松

'''
        中文输出
'''
import re
import urllib.request

reponse=urllib.request.urlopen('http://www.baidu.com')
text=reponse.read().decode('utf-8')
#输出中文
# str='[\u4e00-\u9fa5]'
str='<tittle(.*)'
str2=re.findall(str,text,re.S)
print(str2)
