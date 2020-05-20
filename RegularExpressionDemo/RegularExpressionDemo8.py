#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :RegularExpressionDemo.py
# @Time      :2020/3/24 14:16
# @Author    :青松

'''
        re.S 使 ． 匹配包括换行在内的所有字符

'''
import re

str ='''
       <!DOCTYPE html>
        <html>
        <head>
        <title>文档的标题</title>
        </head>
        
        <body>
        文档的内容......
        </body>
        
        </html>
'''

str2='<title>(.*)</title>'
str3=re.findall(str2,str,re.S)
if str3:
    print(str3)
    # print(str3[0])
else:
    print('null')
