#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :string.py
# @Time      :2020/5/10 11:42
# @Author    :青松


student={'name':'小明','class':20190301,'score':597.5}

print('%-4s同学' % student['name'])
print('%(class)10s班 %(name)-4s同学，总分:%(score)7.2f' % student)
s='{} 班 {} 同学，总分:{}'
print(s.format(student['class'],student['name'],student['score']))
