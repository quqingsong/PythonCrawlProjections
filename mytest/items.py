# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MytestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ip = scrapy.Field()
    # 端口号
    prop = scrapy.Field()
    # 匿名度
    anonymity = scrapy.Field()
    # 类型
    types = scrapy.Field()
    # 位置
    location = scrapy.Field()
    # 响应速度
    speed = scrapy.Field()
    # 最后验证时间
    lasttime = scrapy.Field()
