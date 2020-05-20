#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :chormeDemo2.py
# @Time      :2020/4/10 12:12
# @Author    :青松

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chorme_option=Options()
#无界面显示
# chorme_option.add_argument('--headless')
driver=webdriver.Chrome(options=chorme_option)

driver.get('http://www.baidu.com')
time.sleep(10)
# print(driver.page_source)
print(driver.title)
driver.quit()
# driver.close()
