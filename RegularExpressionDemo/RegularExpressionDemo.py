#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :RegularExpressionDemo.py
# @Time      :2020/3/24 14:16
# @Author    :青松

import re

str='Hello 123 4567 World_This is a Regex Demo '
#输出字符串长度
print(len(str))
#模式匹配
str1='^Hello\s\d{3}\s\d{4}\s\w{10}'
#输出字符串
str2=re.match(str1,str)
print(str2)
print(str2.group())
print(str2.span())

