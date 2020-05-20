#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :printtime.py
# @Time      :2020/5/6 23:22
# @Author    :青松
 
import time


start_time=time.time()
time.sleep(5)
end_time=time.time()
conclude=end_time-start_time

print(end_time-start_time)
print(str(conclude))
