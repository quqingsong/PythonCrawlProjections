#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :startproject.py
# @Time      :2020/5/17 16:10
# @Author    :青松
import scrapy
from scrapy import cmdline

cmdline.execute(["scrapy","crawl","test","-o","1.csv"])
 

