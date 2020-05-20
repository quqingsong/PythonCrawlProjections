#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :xpath.py
# @Time      :2020/4/13 22:49
# @Author    :青松
 

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :XPathTest.py
# @Time      :2020/4/12 0:06
# @Author    :青松

import lxml.etree
import re

html='''
# <div class="dxypage clearfix">
# 	页次：1/513 每页40 文章数20513&nbsp;&nbsp;
# 	<a href="#">
# 		首页
# 	</a>
# 	<a href="#">
# 		上页
# 	</a>
# 	<strong>
# 		1
# 	</strong>
# 	<a href="/list/list_97_2.htm">
# 		2
# 	</a>
# 	<a href="/list/list_97_3.htm">
# 		3
# 	</a>
# 	<a href="/list/list_97_2.htm" title="下页">
# 		下页
# 	</a>
# 	<a href="/list/list_97_513.htm" title="末页">
# 		末页
# 	</a>
# </div>

<span class="state3"><a target="_blank" href="/political/politics/index?id=456812" class="color-hover">莲湖居委会卫生检查</a></span>
'''
mytree=lxml.etree.HTML(html)
# data=mytree.xpath("//*[@class=\"dxypage clearfix\"]/text()")
data=mytree.xpath("//span/a/@href")[0]
print(data)