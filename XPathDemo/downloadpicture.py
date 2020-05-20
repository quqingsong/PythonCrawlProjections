#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :downloadpicture.py
# @Time      :2020/4/16 20:05
# @Author    :青松
 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
import urllib.request

def getimage(imageurl):
    myoption = Options()
    # myoption.add_argument('--headless')
    brower = webdriver.Chrome(options=myoption)
    # #搜索杨幂
    brower.get(imageurl)
    html = brower.page_source
    urllib.request.urlretrieve(imageurl,'jpg/'+str(1)+'.jpg')
    brower.quit()


if __name__=='__main__':
    url='http://tiebapic.baidu.com/forum/w%3D580/sign=4b18c9bf2e01213fcf334ed464e736f8/8ccca71ea8d3fd1f873c5f5c274e251f95ca5f62.jpg'
    getimage(url)
