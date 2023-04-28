#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/27 21:34
# @File : 爬虫request.py
import requests
r = requests.get('https://api.github.com/user',auth=('user', 'pass'))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)