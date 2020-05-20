#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :phantomjsDemo.py
# @Time      :2020/4/10 11:16
# @Author    :青松

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 创建参数设置对象.
chorm_option = Options()
# 无界面化.
chorm_option.add_argument('--headless')
# 配合上面的无界面化.
chorm_option.add_argument('--disable-gpu')
# 设置窗口大小, 窗口大小会有影响.
chorm_option.add_argument('--window-size=1366,768')

# 创建Chrome对象并传入设置信息.
driver = webdriver.Chrome(options=chorm_option)
# 操作这个对象.
driver.get('http://www.baidu.com')
# print(driver.page_source)
print(driver.title)
driver.quit()



