#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :SelectorDemo.py
# @Time      :2020/4/11 23:45
# @Author    :青松
 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import lxml
import lxml.etree

#设置选项参数
myoption=Options()
#添加无界面模式
myoption.add_argument("--headless")
driver=webdriver.Chrome(options=myoption)
driver.get('https://search.51job.com/list/010000%252C020000%252C040000%252C030200%252C180200,000000,0000,00,9,99,python%25E7%2588%25AC%25E8%2599%25AB,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=')
# print(driver.title)
#职位数量
#//*[@id="resultList"]/div[2]/div[4]
html=driver.page_source
mytree=lxml.etree.HTML(html)
'''
  <div class="rt">        ###      outerHtml
    共52条职位
</div>

#resultList > div.dw_tlc > div:nth-child(4)
'''
data=mytree.xpath("//*[@class=\"rt\"]/text()")[0]

# print(type(data))
print("python爬虫师",data)



driver.quit()

