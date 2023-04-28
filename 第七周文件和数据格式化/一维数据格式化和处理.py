#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/6 15:18
# @File : 一维数据格式化和处理.py
# txt = open('f.txt',encoding='utf-8').read()
# ls = txt.split('$')
# print(ls)
# txt.close()
ls = ['china','english','japan']
txt = open('f.txt','a+',encoding='utf-8')
txt.write('&'.join(ls))
