#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :seliniumLogin.py
# @Time      :2020/4/18 17:54
# @Author    :青松

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

myoption=Options()
# myoption.add_argument('--headless')
brower=webdriver.Chrome(options=myoption)
brower.get('http://qzone.qq.com')
brower.switch_to_frame('login_frame')
brower.find_element_by_id('switcher_plogin').click()
brower.find_element_by_id('u').send_keys('1021237024')
brower.find_element_by_id('p').send_keys('qqs2015101.')
brower.find_element_by_id('login_button').click()

