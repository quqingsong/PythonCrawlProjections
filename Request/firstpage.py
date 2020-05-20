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
    table = mytree.xpath('//table[@class="table table-bordered table-striped"]//th/text()')
    print(format(table[0], '<17'), format(table[1], '<7'), format(table[2], '<6'), format(table[3], '<5'),
          format(table[4], '<45'), format(table[5], '<8'), format(table[6], '<20'))
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


if __name__ == '__main__':
    gethtml()