#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Request.py
# @Time      :2020/4/24 20:03
# @Author    :青松

import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


# 首页网页
url = 'https://www.kuaidaili.com/free/'
def gethtmllink(url):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'channelid=bdtg_a10_a10a1; sid=1587797606769203; _ga=GA1.2.1215337714.1587797614; _gid=GA1.2.131695227.1587797614; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1587821033,1587823917,1587896635,1587906494; amplitude_id_476d446d2d57aa9a7764732a26466a97kuaidaili.com=eyJkZXZpY2VJZCI6ImNlNDkwYTBlLTdkNTctNDVkOC04ZTc1LTFmNzRhYmVkNjE2Y1IiLCJ1c2VySWQiOiI4NTJhN2RlMy0xM2E3LTRhOTUtOGJmZC0xZDVmYjFkYTJiZjQiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE1ODc5MDY0OTM5MTksImxhc3RFdmVudFRpbWUiOjE1ODc5MDY2MjM3MjAsImV2ZW50SWQiOjIsImlkZW50aWZ5SWQiOjMyLCJzZXF1ZW5jZU51bWJlciI6MzR9; _gat=1; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1587906624',
            'Host': 'www.kuaidaili.com',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36 Edg/81.0.416.58'
                       }
    myoption = Options()
    # myoption.add_argument('--headless')
    brower = webdriver.Chrome(options=myoption)
    brower.get(url)
    html = brower.page_source
    mytree = etree.HTML(html)
    table = mytree.xpath('//table[@class="table table-bordered table-striped"]//th/text()')
    print(format(table[0], '<17'), format(table[1], '<7'), format(table[2], '<6'), format(table[3], '<5'),
          format(table[4], '<45'), format(table[5], '<8'), format(table[6], '<20'))
    pagecount = mytree.xpath('//div[@id="listnav"]//li[last()-1]/a/text()')[0]
    # print(pagecount)
    urlfirst = 'https://www.kuaidaili.com/free/inha/'
    urllist = []
    for i in range(1, int(pagecount) + 1):
        urllist.append(urlfirst + str(i) + '/')
    # for i in urllist:
    #     print(i)
    brower.quit()
    return urllist


# 多级网页解析
def gethtml(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'channelid=bdtg_a10_a10a1; sid=1587797606769203; _ga=GA1.2.1215337714.1587797614; _gid=GA1.2.131695227.1587797614; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1587821033,1587823917,1587896635,1587906494; amplitude_id_476d446d2d57aa9a7764732a26466a97kuaidaili.com=eyJkZXZpY2VJZCI6ImNlNDkwYTBlLTdkNTctNDVkOC04ZTc1LTFmNzRhYmVkNjE2Y1IiLCJ1c2VySWQiOiI4NTJhN2RlMy0xM2E3LTRhOTUtOGJmZC0xZDVmYjFkYTJiZjQiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE1ODc5MDY0OTM5MTksImxhc3RFdmVudFRpbWUiOjE1ODc5MDY2MjM3MjAsImV2ZW50SWQiOjIsImlkZW50aWZ5SWQiOjMyLCJzZXF1ZW5jZU51bWJlciI6MzR9; _gat=1; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1587906624',
        'Host': 'www.kuaidaili.com',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36 Edg/81.0.416.58'
        }
    myoption = Options()
    # myoption.add_argument('--headless')
    brower = webdriver.Chrome(options=myoption)
    brower.get(url)
    html = brower.page_source
    mytree = etree.HTML(html)

    # ip地址
    ip = mytree.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[1]/text()')
    # 端口号
    prop = mytree.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[2]/text()')
    # 匿名度
    anonymity = mytree.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[3]/text()')
    # 类型
    types = mytree.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[4]/text()')
    # 位置
    location = mytree.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[5]/text()')
    # 响应速度
    speed = mytree.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[6]/text()')
    # 最后验证时间
    lasttime = mytree.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[7]/text()')
    for i in range(0, 15):
        print(format(ip[i], '<17'), format(prop[i], '<7'), format(anonymity[i], ' <6'), format(types[i], ' <7'),
              format(location[i], '<40'), format(speed[i], '<10'), format(lasttime[i], '<2'), )

    brower.quit()

if __name__ == '__main__':
    urls = gethtmllink(url)
    # gethtml(url)
    for u in urls:
        try:
        # print(u)
          gethtml(u)
          print('#############')

        except IndexError:
            pass
