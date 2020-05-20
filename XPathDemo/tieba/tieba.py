#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :tieba.py
# @Time      :2020/4/16 12:00
# @Author    :青松

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
import urllib.request

#获取图片链接
def getimageurl():
    myoption=Options()
    myoption.add_argument('--headless')
    brower=webdriver.Chrome(options=myoption)
   ######################################################################
    # # 禁止图片和css加载
    # prefs = {"profile.managed_default_content_settings.images": 2}
    #
    # myoption.add_experimental_option("prefs", prefs)
    ######################################################################

    # #搜索杨幂
    brower.get('https://tieba.baidu.com/p/6551954897/?pn=1')
    html=brower.page_source
    mytree=etree.HTML(html)
    pagecount=mytree.xpath('//*[@id="thread_theme_5"]/div[1]/ul/li[2]/span[2]/text()')[0]
    # print(pagecount)
    # print(type(pagecount))
    #这里必须转换为int型
    number=eval(pagecount)
    urllist=[]
    for url in range(1,number+1):
        urllist.append('https://tieba.baidu.com/p/6551954897/?pn='+str(url))
    # print(urllist)
    return urllist
def getimage(imageurl):
    myoption = Options()
    myoption.add_argument('--headless')
    brower = webdriver.Chrome(options=myoption)
    # #搜索杨幂
    brower.get(imageurl)
    html = brower.page_source
    mytree = etree.HTML(html)
    data=mytree.xpath('//*[@class="BDE_Image" ]/@src')
    jpgnumber=1
    for list in data:
        # print(list)
        urllib.request.urlretrieve(list,'jpg/'+str(jpgnumber)+'.jpg')
        jpgnumber+=1
        # urllib.urlretrieve(list,'jpg/'+str(jpgnumber)+'.jpg')

if __name__=='__main__':
    imageurls=getimageurl()
    for u in imageurls:
        getimage(u)

