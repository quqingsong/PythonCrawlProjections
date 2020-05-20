#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test.py
# @Time      :2020/3/25 10:54
# @Author    :青松

'''
        str='Hello 123 4567 World_This is a Regex Demo '
        #输出字符串长度
        print(len(str))
        #模式匹配,()中的是子式，所以用1表示
        str2='^He.*(\d+).*Demo$'
        #输出字符串
        str3=re.match(str2,str)
        print(str3)
'''
import re

str = 'Hello 1234567 World_This is a Demo'
str2='^He.*(\d+).*Demo$'
str3 = re.match(str2, str)
print(str3)
print(str3.group(1))