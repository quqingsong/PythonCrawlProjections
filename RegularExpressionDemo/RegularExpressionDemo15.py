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
# text='''
#   <div class="dxypage clearfix">
# 	页次：1/513 每页40 文章数20513&nbsp;&nbsp;
# 	<a href="#">
# 		首页
# 	</a>
# 	<a href="#">
# 		上页
# 	</a>
# 	<strong>
# 		1
# 	</strong>
# 	<a href="/list/list_97_2.htm">
# 		2
# 	</a>
# 	<a href="/list/list_97_3.htm">
# 		3
# 	</a>
# 	<a href="/list/list_97_2.htm" title="下页">
# 		下页
# 	</a>
# 	<a href="/list/list_97_513.htm" title="末页">
# 		末页
# 	</a>
# </div>
# '''
url='https://www.jb51.net/list/list_97_1.htm'

reponse=urllib.request.urlopen(url)
text1=reponse.read().decode('utf-8')
# str2='<a.*?>(.*)</a>'
str2='<div class="dxypage clearfix">\n\t页次：1/(.*)每页'
str3=re.findall(str2,text1,re.S)
if str3:
    print(str3)
    # print(str3[0])
else:
    print('没有')
