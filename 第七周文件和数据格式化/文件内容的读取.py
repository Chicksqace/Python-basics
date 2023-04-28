#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/5 16:06
# @File : 文件内容的读取.py
tf=open("f.txt",'rt',encoding='utf-8')
print(tf.read(2))
tf.close()

tf=open("f.txt",'rt',encoding='utf-8')
print(tf.readline())
tf.close()

tf=open("f.txt",'rt',encoding='utf-8')
print(tf.readlines(1))
tf.close()