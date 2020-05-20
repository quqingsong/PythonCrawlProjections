# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['http://kuaidaili.com/']

    def parse(self, response):
        pass
