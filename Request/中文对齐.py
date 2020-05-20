#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :中文对齐.py
# @Time      :2020/5/17 0:24
# @Author    :青松
 
# tplt = "{0:{3}^10}\t{1:{3}^10}\t{2:^10}"
#     print(tplt.format("学校名称", "位置", "分数", chr(12288)))
#     for i in range(num):
#         u = ulist[i]
#         print(tplt.format(u[0], u[1], u[2], chr(12288)))


s1 = 'long long long .'
s2 = 'short.'

print('%-30s%-20s' % (s1, s2))  # '%-30s' 含义是 左对齐，且占用30个字符位
print('%-30s%-20s' % (s2, s1))

# long long long .              short.
# short.                        long long long .

s1 = 'long long long .'
s2 = 'short.'
print ('{:>30}{:>20}' .format(s1,s2)) #{:30d}含义是 右对齐，且占用30个字符位
print ('{:<30}{:<20}' .format(s1,s2)) #{:<30d}含义是 左对齐，且占用30个字符位
print ('{:^30}{:^20}' .format(s1,s2)) #{:<30d}含义是 居中对齐，且占用30个字符位

#               long long long .              short.
# long long long .              short.
#        long long long .              short.


print('{0:{1}^9}\t'.format(10,chr(12288)),end = '') # 居中对齐
print('{0:{1}<9}\t'.format(10,chr(12288)),end = '') # 左对齐    用chr(12288)去填充，即这里的{1}
