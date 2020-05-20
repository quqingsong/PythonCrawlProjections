# -*- coding: utf-8 -*-
import scrapy
import mytest.items


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/']
    count = 1
    '''
    parse(response)
    这个其实默认的回调函数
    负责处理response并返回处理的数据以及跟进的url
    该方法以及其他的Request回调函数必须返回一个包含Request或Item的可迭代对象
    '''

    def parse(self, response):
        # 字典的形式
        trlist = response.xpath('//table[@class="table table-bordered table-striped"]/tbody//tr')
        for list in trlist:
            kuaidailiItems = mytest.items.MytestItem()
            kuaidailiItems["ip"] = list.xpath('./td[1]/text()').extract()
            kuaidailiItems["prop"] = list.xpath('./td[2]/text()').extract()
            kuaidailiItems["anonymity"] = list.xpath('./td[3]/text()').extract()
            kuaidailiItems["types"] = list.xpath('./td[4]/text()').extract()
            kuaidailiItems["location"] = list.xpath('./td[5]/text()').extract()
            kuaidailiItems["speed"] = list.xpath('./td[6]/text()').extract()
            kuaidailiItems["lasttime"] = list.xpath('./td[7]/text()').extract()
            yield kuaidailiItems

        # 翻页爬取
        if self.count <5:
            self.count += 1
        next_url = "https://www.kuaidaili.com/free/" + "inha/" + str(self.count) + "/"
        yield scrapy.Request(next_url, callback=self.parse)
