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
    <div class="col-md-8">
                <h1>
                    <a href="/" style="text-decoration: none">Quotes to Scrape</a>
                </h1>
            </div>
            
            <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
'''

reponse=urllib.request.urlopen('http://quotes.toscrape.com/')
text1=reponse.read().decode('utf-8')
# str2='<a.*?>(.*)</a>'
str2='<div.*<a href="/" style="text-decoration: none">(.*)</a>.*</h1>'
str22='<span class="text" itemprop="text">(.*)</span>.*by <small'
str3=re.findall(str2,text1,re.S)
if str3:
    print(str3[0])
    # print(str3[0])
else:
    print('没有')
