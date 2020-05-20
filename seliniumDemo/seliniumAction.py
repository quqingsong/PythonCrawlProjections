#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :seliniumAction.py
# @Time      :2020/4/21 14:37
# @Author    :青松

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

brower=webdriver.Chrome()
brower.get('https://www.baidu.com/')
brower.implicitly_wait(10)
#(By.ID,'kw')这是一个元组
inputs=WebDriverWait(brower,15,0.5).until(EC.presence_of_element_located((By.ID,'kw')))
inputs.send_keys('伊成')
brower.find_element_by_id('su').click()

if brower.find_element_by_class_name('nums').is_displayed():
    print(brower.find_element_by_class_name('nums').text)

time.sleep(10)
brower.quit()

