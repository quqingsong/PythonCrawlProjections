#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :RegularExpressionDemo.py
# @Time      :2020/3/24 14:16
# @Author    :青松

'''
        .*数据匹配任意字符

        *	匹配前面的子表达式零次或多次。要匹配 * 字符，请使用 \*。
        +	匹配前面的子表达式一次或多次。要匹配 + 字符，请使用 \+。
        .	匹配除换行符 \n 之外的任何单字符。要匹配 . ，请使用 \. 。
'''
import re

str='Hello 123 4567 World_This is a Regex Demo '
#输出字符串长度
print(len(str))
#模式匹配,()中的是子式，所以用1表示
str1='^Hello.*\sWorld'
#输出字符串
str2=re.match(str1,str)
# print(str2)
print(str2.group())
print(str2.span())

