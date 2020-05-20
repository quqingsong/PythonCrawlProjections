#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :threadingDemo.py
# @Time      :2020/5/2 21:27
# @Author    :青松
 
import threading
import time


def gata(names,number):
    for i in range(number):
        time.sleep(1)
        print(names,"第",str(i+1),"次\n")
def main():
    mytread=threading.Thread(target=gata,args=("张三",5,))
    mytread2=threading.Thread(target=gata,args=("李四",5,))
    mytread.start()
    mytread2.start()
    mytread.join()
    mytread2.join()
if __name__=="__main__":
    main()
