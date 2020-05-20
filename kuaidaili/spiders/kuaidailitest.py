# -*- coding: utf-8 -*-
import scrapy
import kuaidaili.items
class KuaidailitestSpider(scrapy.Spider):
    '''
     name
    定 义爬虫名字，我们通过命令启动的时候用的就是这个名字，这个名字必须是唯一的
    allowed_domains
    包含了spider允许爬取的域名列表。当offsiteMiddleware启用时，域名不在列表中URL不会被访问
    所以在爬虫文件中，每次生成Request请求时都会进行和这里的域名进行判断
    start_urls
    起始的url列表
    这里会通过spider.Spider方法中会调用start_request循环请求这个列表中每个地址。
    '''
    name = 'kuaidailitest'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/']
    count=1
    '''
    parse(response)
    这个其实默认的回调函数
    负责处理response并返回处理的数据以及跟进的url
    该方法以及其他的Request回调函数必须返回一个包含Request或Item的可迭代对象
    '''
    def parse(self, response):
        #字典的形式
        trlist=response.xpath('//table[@class="table table-bordered table-striped"]/tbody//tr')
        for list in trlist:
            kuaidailiItems = kuaidaili.items.KuaidailiItem()
            kuaidailiItems["ip"]=list.xpath('./td[1]/text()').extract()
            kuaidailiItems["prop"]= list.xpath('./td[2]/text()').extract()
            kuaidailiItems["anonymity"]= list.xpath('./td[3]/text()').extract()
            kuaidailiItems["types"]=  list.xpath('./td[4]/text()').extract()
            kuaidailiItems["location"]= list.xpath('./td[5]/text()').extract()
            kuaidailiItems["speed"]= list.xpath('./td[6]/text()').extract()
            kuaidailiItems["lasttime"]= list.xpath('./td[7]/text()').extract()
            yield kuaidailiItems

        #翻页爬取
        if self.count<3:
            self.count+=1
        next_url="https://www.kuaidaili.com/free/"+"inha/"+str(self.count)+"/"
        yield scrapy.Request(next_url,callback=self.parse)
