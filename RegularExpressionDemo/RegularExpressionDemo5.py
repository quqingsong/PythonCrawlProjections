#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :RegularExpressionDemo.py
# @Time      :2020/3/24 14:16
# @Author    :青松

'''
        re.S 使 ． 匹配包括换行在内的所有字符

'''
import re

str ='Hello 1234567 World_This\n is a Regex Demo'
#输出字符串长度
print(len(str))
#模式匹配,()中的是子式，所以用1表示,注意  $必须是末尾
str2='^He.*?(\d+).*Demo$'
#输出字符串
str3=re.match(str2,str,re.S)
print(str3)
print(str3.group())
print(str3.group(1))
print(str3.span())

