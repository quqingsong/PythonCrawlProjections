#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :douyu.py
# @Time      :2020/5/19 18:04
# @Author    :青松
 

import json

with open("1.json","r") as file:
    jsonfile=file.read()
# print(jsonfile)
jsonData =jsonfile
datas = json.loads(jsonData)["data"]["rl"]
# print(datas["nn"])
for data in datas:
    print(data["nn"])

# s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
# print(s.keys())
# print(s["name"])
# print(s["type"]["name"])
# print(s["type"]["parameter"][1])
'''
dict_keys(['name', 'type'])
test
seq
2
'''