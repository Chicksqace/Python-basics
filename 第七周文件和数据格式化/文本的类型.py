#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/5 15:38
# @File : 文本的类型.py
tf=open("f.txt",'rt',encoding='utf-8')
print(tf.readline())
tf.close()
tf=open("f.txt",'rb')
print(tf.readline())
tf.close()