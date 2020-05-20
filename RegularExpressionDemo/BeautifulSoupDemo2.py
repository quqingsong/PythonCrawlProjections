#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :RegularExpressionDemo.py
# @Time      :2020/3/24 14:16
# @Author    :青松

'''
        re.S 使 ． 匹配包括换行在内的所有字符

'''
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all('ul'))
# print(type(soup.find_all('ul')[0]))

# for ul in soup.find_all('ul'):
#     print(ul.find_all('li'))

# print(soup.find_all(attrs={'id': 'list-1'}))
# print('#########################################################')
# print(soup.find_all(attrs={'class': 'element'}))

# print('#########################################################')
#
# print(soup.find_all(text='Foo'))
#
# print(soup.select('ul li'))
#
# for li in soup.select('li'):
#     print(li.get_text())

for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])