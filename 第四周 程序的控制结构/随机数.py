#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/22 20:23
# @File : 随机数.py
import random
# a=random.seed(3)
# print(random.random())
# print(random.random())
# print(random.random())
# print(random.random())
# print(random.random())
# print(random.random())
# print(random.random())
# print(random.random())
# print(random.random())
# print(random.random())
# a=random.seed(3)
# print('随机数种子',random.random())
# a=random.seed(3)
# print('随机数种子',random.random())
arr=[]
for i in range(10):
    arr.append(random.randint(0,10))
# 随机抽一个数
print(random.choice(arr))
print(arr)
random.shuffle(arr)
# 元素重新大乱
print(arr)