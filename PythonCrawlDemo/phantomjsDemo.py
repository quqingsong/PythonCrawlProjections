#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :phantomjsDemo.py
# @Time      :2020/4/10 12:10
# @Author    :青松

'''
    phantomjs这种版本已经弃用，请使用Chorme无头版本
    UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead
  warnings.warn('Selenium support for PhantomJS has been deprecated, please use headless '
'''

from selenium import webdriver

path=r'C:\MyInstallInformation\phantomjs-2.1.1-windows\bin\phantomjs.exe'
driver=webdriver.PhantomJS(path)
driver.get('http://www.baidu.com')
print(driver.title)
