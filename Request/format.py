#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :format.py
# @Time      :2020/4/26 0:16
# @Author    :青松

# # 代码
# print("|", format("Ursula", "*>20"), "|")  # 左对齐
# print("|", format("Ursula", "*^20"), "|")  # 居中对齐
# print("|", format("Ursula", "*<20"), "|")  # 右对齐
#
# # 运行结果
# | ** ** ** ** ** ** ** Ursula |
# | ** ** ** *Ursula ** ** ** * |
# | Ursula ** ** ** ** ** ** ** |
print(format('632423','*>10'),format('632423','*^10'))
print(format('6323','*^10'))
print(format('632423','*<10'),format('632423','*<10'))
print(format('中国','*<10'),format('中国','*<10'))
print(format('中国','<10'),format('中国','<10'))

for i in range(1,7):
    print(i)
