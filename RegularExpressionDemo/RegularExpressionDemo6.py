#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :RegularExpressionDemo.py
# @Time      :2020/3/24 14:16
# @Author    :青松

'''
        re.S 使 ． 匹配包括换行在内的所有字符

'''
import re

str ='''
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
        <html>
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=gb2312">
        <title>无标题文档</title>
        </head>
        
        <body>
        <form name="form1" method="post" action="">
          <p>姓名:lizhizhe2000(彬彬 )    
        </p>
          <p>地址格式等)，它具有用来检查给出的字符串是否符合规则的属性和方法。 <br>
          除此之外，你用RegExp构造器建立的个别正则表达式对象的属性，就已经预先定义好了正则表达式 </p>
          <p><img src="protfield.gif" width="16" height="16">
          <img src="protmethod.gif" width="16" height="16"></p>
        </form>
        </body>
        </html>
'''
#输出字符串长度
print(len(str))
#模式匹配,()中的是子式，所以用1表示,注意  $必须是末尾
# str2='<title>(.*?)</title>'
#输出字符串RegularExpressionDemo6.py
str2='form1<p>.*?(.*)</p>'
str3=re.findall(str2,str,re.S)
print(str3)
