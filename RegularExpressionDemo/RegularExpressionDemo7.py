#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :RegularExpressionDemo.py
# @Time      :2020/3/24 14:16
# @Author    :青松

import re



def main():
    content = 'Hello, I am Jerry, from Chongqing, a montain city, nice to meet you……'
    regex = re.compile('\w*o\w*')#查询所有包含o的单词
    x = regex.findall(content)
    print(x)


if __name__ == '__main__':
    main()
# ['Hello', 'from', 'Chongqing', 'montain', 'to', 'you']