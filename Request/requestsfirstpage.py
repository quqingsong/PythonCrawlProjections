#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :requestsfirstpage.py
# @Time      :2020/5/9 16:18
# @Author    :青松


# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Request.py
# @Time      :2020/4/24 20:03
# @Author    :青松

import requests
from lxml import etree

url = 'https://www.kuaidaili.com/free/'


def gethtml():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    # response = requests.get(url, headers=headers)
    # 成功访问
    # print(response.text)
    # print(response.headers)
    # html = response.text
    pathname="D:\PycharmProjects\kuaidaili\国内高匿免费HTTP代理IP - 快代理.html"
    with open(pathname,"rb") as f:
        # for line in f:
        data=f.read()
        # print(data)
    mytree = etree.HTML(data)
    trlist = mytree.xpath('//table[@class="table table-bordered table-striped"]//th/text()')
    print(format(trlist[0], '<17'), format(trlist[1], '<7'), format(trlist[2], '<6'), format(trlist[3], '<5'),
          format(trlist[4], '<45'), format(trlist[5], '<8'), format(trlist[6], '<20'))

    trlists = mytree.xpath('//table[@class="table table-bordered table-striped"]/tbody//tr')
    # print(trlists)
    for tr in trlists:
        # ip地址
        ip = tr.xpath('./td[1]/text()')[0]
        # print(ip)
        # # 端口号
        prop = tr.xpath('./td[2]/text()')[0]
        # print(format(prop, '<7'), end='')
        # # 匿名度
        anonymity = tr.xpath('./td[3]/text()')[0]
        # print(format(anonymity, '<6'), end='')
        # # 类型
        types = tr.xpath('./td[4]/text()')[0]
        # print(format(types, '<7'), end='')
        # # 位置
        location = tr.xpath('./td[5]/text()')[0]
        # print(format(location, '<40'), end='')
        # # 响应速度
        speed = tr.xpath('./td[6]/text()')[0]
        # print(format(speed, '<10'), end='')
        # # 最后验证时间
        lasttime = tr.xpath('./td[7]/text()')[0]
        # print(format(lasttime, '<2'), end='')
        print(format(ip, '<17'),format(prop, '<7'),format(anonymity, '<6'),format(types, '<7'),format(location, '<40'),format(speed, '<10'),format(lasttime, '<2'))

if __name__ == '__main__':
    gethtml()