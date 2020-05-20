#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :文件下载.py
# @Time      :2020/5/7 16:58
# @Author    :青松
 
import os
import urllib.request


url="https://rpic.douyucdn.cn/live-cover/appCovers/2018/10/09/4403598_20181009234622_small.jpg"
def download(url):
    #创建目录
    os.makedirs("jpg")
    #下载图片
    urllib.request.urlretrieve(url,"jpg/"+"1.jpg")

if __name__=="__main__":
    download(url)
    print("下载完成")