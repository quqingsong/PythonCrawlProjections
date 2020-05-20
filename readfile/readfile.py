#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :readfile.py
# @Time      :2020/5/2 12:06
# @Author    :青松
 
#方法一

# filepath='students.txt'
# readfile=open(filepath,'rb')
# print(readfile.read().decode('utf-8',errors='ignore'))

#方法二

import re
filepath='students.txt'
readfile=open(filepath,'rb')
mylist=readfile.readlines() #readlines()是读取一行
print(len(mylist))  #计算列表长度
agelist=[]
for line in mylist:
    line=line.decode('utf-8',errors='ignore')

    # line=line.decode('gbk',errors='ignore')
    # print(line)
    linelist=line.split('\t')
    # linelist=re.split('\t',line)
    # del linelist[4,5]
    # print(linelist)
    agelist.append(linelist)#每一个元素都是列表

readfile.close()

agelist.sort(key=lambda x:eval(x[1]))

savefile=open('age.txt','w')
for age in agelist:
    savefile.write(str(age)+'\n')
    print(age)


savefile.close()

